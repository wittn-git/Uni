public class TreeNode {

    private TreeNode left;
    private TreeNode right;
    private final int value;

    public TreeNode(int val) {
      this.value = val;
      this.left = null;
      this.right = null;
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
      return Integer.toString(this.value);
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
  
    public void insert(int x) {
      if(this.value != x){
        if(x>this.value){
          if(this.hasRight()){
            this.right.insert(x);
          }else{
            this.right = new TreeNode(x);
          }
        }
        if(x<this.value){
          if(this.hasLeft()){
            this.left.insert(x);
          }else{
            this.left = new TreeNode(x);
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