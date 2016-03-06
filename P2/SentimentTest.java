import shared.Instance;
import java.lang.StringBuilder;
import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.util.Scanner;


class SentimentTest {

  public static void main(String[] args) {
      System.out.println(initializeInstances("5")[0]);
  } 

  private static Instance[] initializeInstances(String bagSize) {
      double[][][] attributes = new double[3000][][]; // 3000 instances

      try {
          BufferedReader br = new BufferedReader(new FileReader(new File("datasets/bag" + bagSize + ".data")));

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
