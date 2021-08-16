public class TreeNode {

    private TreeNode left;
    private TreeNode right;
    private final int value;
    private int prior;
    private String text;

    public TreeNode(int val, int prior, String text) {
      this.value = val;
      this.left = null;
      this.right = null;
      this.prior = prior;
      this.text = text;
    }
  
    public TreeNode(int val, TreeNode left, TreeNode right) {
      this.value = val;
      this.left = left;
      this.right = right;
    }
    public int getValue() {
      return this.value;
    }
  
    public String getValueString() {
      //return String.format("%s_%d", text, prior);
      //return String.format("%s", text);
      return String.format("%d", prior);
    }

    public boolean hasLeft() {
      return this.left != null;
    }

    public boolean hasRight() {
      return this.right != null;
    }
  	
    public TreeNode getLeft() {
      return this.left;
    }
    
    public TreeNode getRight() {
      return this.right;
    }
  
    public void insert(int x, int prior, String text) {
      if(this.value != x){
        if(x>this.value){
          if(this.hasRight()){
            this.right.insert(x, prior, text);
          }else{
            this.right = new TreeNode(x, prior, text);
          }
        }
        if(x<this.value){
          if(this.hasLeft()){
            this.left.insert(x, prior, text);
          }else{
            this.left = new TreeNode(x, prior, text);
          }
        }
      }
    }
  
    public int toDot(StringBuilder str, int nullNodes) {
      if(this.hasLeft()) {
        str.append(this.getValueString() + " -> " + this.left.getValueString() + ";"
          + System.lineSeparator());
        nullNodes = this.left.toDot(str, nullNodes);
      } else {
        str.append("null" + nullNodes + "[shape=point]" + System.lineSeparator()
          + this.getValueString() + " -> null" + nullNodes + ";" + System.lineSeparator());
        nullNodes += 1;
      }
      if(this.hasRight()) {
        str.append(this.getValueString() + " -> " + this.right.getValueString() + ";"
          + System.lineSeparator());
        nullNodes = this.right.toDot(str, nullNodes);
      } else {
        str.append("null" + nullNodes + "[shape=point]" + System.lineSeparator()
          + this.getValueString() + " -> null" + nullNodes + ";" + System.lineSeparator());
        nullNodes += 1;
      }
      return nullNodes;
    }
  
  }