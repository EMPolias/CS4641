Raphael Gontijo Lopes
903062081

CS 4641 - Machine Learning

A description of the dataset and the optimization problems used can be found in
the analysis pdf
The links for the dataset source is below:

Sentiment Labelled Sentences
https://archive.ics.uci.edu/ml/datasets/Sentiment+Labelled+Sentences

The dataset is included in my submission, along with my code. It has been
pre-processed with defined bag sizes to easily use it in the java code.

To run any of the experiments mentioned in the analysis, you must have
installed java 8 with the ABAGAIL package in the same directory. I also provide
the unmodified jar.
Then you can simply:

$ javac -cp ABAGAIL.jar:. ExperimentName.java
$ java -cp ABAGAIL.jar:. ExperimentName

Note that many of the training sessions for the Sentiment experiment can take a
long time. If you want to run just one of the experiments, you can modify the
source by commenting out in the main method:

public void main(String[] args) {
  // experiment1();
  experiment2();
}

Alternatively, all of my experiment runs are being submitted under experiments/.
Also included are my plots for the experiments.
