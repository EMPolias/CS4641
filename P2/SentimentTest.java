import shared.Instance;
import shared.SumOfSquaresError;
import shared.ErrorMeasure;
import shared.DataSet;
import opt.OptimizationAlgorithm;
import opt.RandomizedHillClimbing;
import func.nn.backprop.BackPropagationNetwork;
import func.nn.backprop.BackPropagationNetworkFactory;
import opt.example.NeuralNetworkOptimizationProblem;
import java.lang.StringBuilder;
import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.util.Scanner;
import java.text.DecimalFormat;


class SentimentTest {

  private static double train_size = 2100;
  private static double test_size = 900;
  // private static int trainingIterations = 2800;
  private static BackPropagationNetworkFactory factory = new BackPropagationNetworkFactory();
  private static ErrorMeasure measure = new SumOfSquaresError();
  private static DecimalFormat df = new DecimalFormat("0.000");

  public static void main(String[] args) {
      // experiment1(2800);
      // experiment1(5500);
      // experiment2(6000, "200");
  } 

  private static void experiment1(int trainingIterations) {
      // EXPERIMENT 1 - Sanity check: making sure we have a reasonable bag size.
      String[] bagSizes = {"5", "10", "20", "40", "80", "120", "160", "200", "300", "500", "700", "850", "1000", "1200"};
      
      for (String bagSize : bagSizes) {
          int bagSizeInt = Integer.parseInt(bagSize);

          // Set up dataset.
          Instance[] train_instances = initializeInstances(bagSize, false);
          Instance[] test_instances = initializeInstances(bagSize, true);
          DataSet set = new DataSet(train_instances);
  
          // Set up optmization problem
          BackPropagationNetwork network = factory.createClassificationNetwork(
              new int[] {bagSizeInt, 10, 1});
          NeuralNetworkOptimizationProblem nnop = new NeuralNetworkOptimizationProblem(set, network, measure);
          OptimizationAlgorithm oa = new RandomizedHillClimbing(nnop);

          // Start Training
          double start = System.nanoTime(), end, trainingTime, testingTime, correct = 0, incorrect = 0;
          System.out.println("Training NN with RHC and bagSize=" + bagSize);
          train(oa, network, test_instances, trainingIterations);
          end = System.nanoTime();

          trainingTime = end - start;
          trainingTime /= Math.pow(10,9);

          Instance optimalInstance = oa.getOptimal();
          network.setWeights(optimalInstance.getData());

          double predicted, actual;
          start = System.nanoTime();
          for(int j = 0; j < test_instances.length; j++) {
              network.setInputValues(test_instances[j].getData());
              network.run();

              predicted = Double.parseDouble(test_instances[j].getLabel().toString());
              actual = Double.parseDouble(network.getOutputValues().toString());
              double trash = Math.abs(predicted - actual) < 0.5 ? correct++ : incorrect++;

          }
          end = System.nanoTime();
          testingTime = end - start;
          testingTime /= Math.pow(10,9);

          System.out.println("Final Results:");
          System.out.println("Correctly classified: " + correct);
          System.out.println("Incorrectly classified: " + incorrect);
          System.out.println("Percent: " + df.format(correct/(correct+incorrect)*100));
          System.out.println("Training time: " + df.format(trainingTime));
          System.out.println("Testing time: " + df.format(testingTime));
      }
  }

  private static void experiment2(int trainingIterations, String bagSize) {
      // EXPERIMENT 2 - Random restarting RHC
      int[] numberOfRestarts = {1, 2, 3, 5, 8, 10, 15, 20};

      for (int numberOfRestart : numberOfRestarts) {
          int bagSizeInt = Integer.parseInt(bagSize);

          // Set up dataset.
          Instance[] train_instances = initializeInstances(bagSize, false);
          Instance[] test_instances = initializeInstances(bagSize, true);
          DataSet set = new DataSet(train_instances);
  
          System.out.println("Training multiple NNs with RHC and bagSize=" + bagSize + " and numberOfRestarts=" + numberOfRestart);
          double bestError = 100000;
          OptimizationAlgorithm bestoa = null;
          double start = System.nanoTime(), end = 0, trainingTime = 0, testingTime = 0;
          
          for (int i = 0; i < numberOfRestart; i++) {
              // Set up optmization problem
              BackPropagationNetwork network = factory.createClassificationNetwork(
                  new int[] {bagSizeInt, 10, 1});
              NeuralNetworkOptimizationProblem nnop = new NeuralNetworkOptimizationProblem(set, network, measure);
              OptimizationAlgorithm oa = new RandomizedHillClimbing(nnop);

              // Start Training
              double error = train(oa, network, test_instances, trainingIterations);

              if (error < bestError) {
                  bestError = error;
                  bestoa = oa;
              }
          }

          end = System.nanoTime();
          trainingTime = end - start;
          trainingTime /= Math.pow(10,9);
          
          if (bestoa == null) throw new Error("bestoa not initialized");
          Instance optimalInstance = bestoa.getOptimal();
          BackPropagationNetwork network = factory.createClassificationNetwork(
              new int[] {bagSizeInt, 10, 1});
          network.setWeights(optimalInstance.getData());

          double correct = 0, incorrect = 0;
          double predicted, actual;
          start = System.nanoTime();
          for(int j = 0; j < test_instances.length; j++) {
              network.setInputValues(test_instances[j].getData());
              network.run();

              predicted = Double.parseDouble(test_instances[j].getLabel().toString());
              actual = Double.parseDouble(network.getOutputValues().toString());
              double trash = Math.abs(predicted - actual) < 0.5 ? correct++ : incorrect++;
          }

          end = System.nanoTime();
          testingTime = end - start;
          testingTime /= Math.pow(10,9);

          System.out.println("Final Results:");
          System.out.println("Train Error: " + df.format(bestError));
          System.out.println("Test Percent Correct: " + df.format(correct/(correct+incorrect)*100));
          System.out.println("Training time: " + df.format(trainingTime));
          System.out.println("Testing time: " + df.format(testingTime));
      }
  }

  private static double train(OptimizationAlgorithm oa,
                            BackPropagationNetwork network,
                            Instance[] testing,
                            int trainingIterations) {
      double length = train_size;
      double incorrect = 0;
      for(int i = 0; i < trainingIterations; i++) {
          incorrect = 0;
          oa.train();

          double error = 0;
          for(int j = 0; j < testing.length; j++) {
              network.setInputValues(testing[j].getData());
              network.run();

              Instance output = testing[j].getLabel(), example = new Instance(network.getOutputValues());
              example.setLabel(new Instance(Double.parseDouble(network.getOutputValues().toString())));
              error += measure.value(output, example);
              incorrect += Math.abs(Double.parseDouble(output.toString()) - Double.parseDouble(example.getLabel().toString())) < 0.5 ? 0 : 1;
          }

          // if (i % 100 == 0) 
          // if (i == trainingIterations - 1) 
            // System.out.println("\tIteration " + i + " error: " + df.format(incorrect/length*100));
      }
      return (incorrect/length*100);
  }

  private static Instance[] initializeInstances(String bagSize, Boolean test_set) {
      int num_instances = 2100;
      if (test_set) num_instances = 900;

      double[][][] attributes = new double[num_instances][][];

      try {
          String filename = "datasets/bag" + bagSize + ".data";
          if (test_set) filename = "datasets/bag" + bagSize + "_test.data";

          BufferedReader br = new BufferedReader(new FileReader(new File(filename)));

          for(int i = 0; i < attributes.length; i++) {
              Scanner scan = new Scanner(br.readLine());
              scan.useDelimiter(", ");

              attributes[i] = new double[2][];
              attributes[i][0] = new double[Integer.parseInt(bagSize)]; // bagSize attributes
              attributes[i][1] = new double[1];

              for(int j = 0; j < Integer.parseInt(bagSize); j++)
                  attributes[i][0][j] = Double.parseDouble(scan.next());

              attributes[i][1][0] = Double.parseDouble(scan.next());
          }
      }
      catch(Exception e) {
          e.printStackTrace();
      }

      Instance[] instances = new Instance[attributes.length];

      for(int i = 0; i < instances.length; i++) {
          instances[i] = new Instance(attributes[i][0]);
          instances[i].setLabel(new Instance(attributes[i][1][0] < .5 ? 0 : 1));
      }

      return instances;
  }

}
