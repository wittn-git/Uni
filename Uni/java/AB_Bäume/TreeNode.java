import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class TreeNode {

    private final String value;
    private List<TreeNode> children;
    private String id;

    public TreeNode(String val) {
      this.value = val;
      children = new ArrayList<TreeNode>();
      id = createID();
    }
  
    public TreeNode(String val, List<TreeNode> children) {
      this.value = val;
      this.children = children;
      id = createID();
    }

    public String createID(){
      Random r = new Random();
      return Integer.toString(r.nextInt(100000));
    }

    public String getID() {
      return id;
    }
  
    public void insert(TreeNode child) {
      children.add(child);
    }

    public void insert(Integer value) {
      children.add(new TreeNode(Integer.toString(value)));
    }
  
    public int toDot(StringBuilder str, int nullNodes) {
      str.append(String.format("%s [label=\"%s\"]", id, value)+ System.lineSeparator());
      for(TreeNode child: children){
        str.append(this.getID() + " -> " + child.getID() + ";"
          + System.lineSeparator());
        nullNodes = child.toDot(str, nullNodes);
      }
      return nullNodes;
    }
  
  }