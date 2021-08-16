import java.io.*;

public class Tree {

  private TreeNode root;

  public Tree() {
    this.root = null ;
  }

  public boolean isEmpty() {
    return this.root == null ;
  }

  public void insert(int x, int prior, String text) {
    if(this.root == null) this.root = new TreeNode(x, prior, text);
    else this.root.insert(x, prior, text);
  }

  private String toDot() {
    if ( this.isEmpty ()) {
      return "digraph { null[shape=point]; }";
    }
    StringBuilder str = new StringBuilder ();
    this.root.toDot (str, 0);
    return "digraph { " + System.lineSeparator ()
      + "graph[ordering=\"out\"]; " + System.lineSeparator ()
      + str.toString ()
      + "}" + System.lineSeparator ();
  }

  public boolean writeToFile(int n) {
    try {
        FileWriter fileWriter = new FileWriter(String.format("d%d.dot", n));
        fileWriter.write(this.toDot());
        fileWriter.close();
    } catch (IOException e) {
        e.printStackTrace();
        return false;
    }
    return true;
  }

}