import shared.Instance;
import java.lang.StringBuilder;
import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;


class SentimentReader {

  private static Instance[] initializeInstances() {
    


  }

  private static ArrayList<Instance> getDataFromFile(String fileName) {
    ArrayList<Instance> data = new ArrayList<Instance>();

    try {
      BufferedReader br = new BufferedReader(new FileReader(new File(fileName)));

      String review = "";
      String line;

      while ((line = br.readLine()) != null) {
        if (line[line.length() - 2] == '0' || line[line.length() - 2] == '1') {
          review += line.substring(0, line.length() - 2);
          Character label = line[line.length() - 2];
          Instance
        } else {
          review += line;
        }
      }
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

}
