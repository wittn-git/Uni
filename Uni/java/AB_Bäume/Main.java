public class Main {

    public static void main(String[] args) {
      t1();
      t2();
      t3();
      t4();
      t5();
    }

    public static void t1(){
      Tree tree = new Tree();
      TreeNode[] basenodes = new TreeNode[4];
      String[] values = new String[]{"1,3,5", "9,11,13", "17,19,21", "25,27,29"};
      int[][] children = new int[][]{{1,3,5,7}, {9,11,13,15}, {17,19,21,23},{25,27,29, 31}};
      for(int i=0; i<4; i++){
        TreeNode node = new TreeNode(values[i]);
        for(int j=0; j<children[i].length; j++){
          node.insert(children[i][j]);
        }
        basenodes[i] = node;
      }
      TreeNode t1 = new TreeNode("7");
      t1.insert(basenodes[0]);
      t1.insert(basenodes[1]);
      TreeNode t2 = new TreeNode("23");
      t2.insert(basenodes[2]);
      t2.insert(basenodes[3]);
      TreeNode root = new TreeNode("15");
      root.insert(t1);
      root.insert(t2);
      tree.putRoot(root);
      tree.writeToFile(0);
    }

    public static void t2(){
      Tree tree = new Tree();
      TreeNode[] basenodes = new TreeNode[4];
      String[] values = new String[]{"1,3,5", "11,13", "17,19,21", "25,27,29"};
      int[][] children = new int[][]{{1,3,5,7}, {11,13,15}, {17,19,21,23},{25,27,29, 31}};
      for(int i=0; i<4; i++){
        TreeNode node = new TreeNode(values[i]);
        for(int j=0; j<children[i].length; j++){
          node.insert(children[i][j]);
        }
        basenodes[i] = node;
      }
      TreeNode t1 = new TreeNode("7");
      t1.insert(basenodes[0]);
      t1.insert(basenodes[1]);
      TreeNode t2 = new TreeNode("23");
      t2.insert(basenodes[2]);
      t2.insert(basenodes[3]);
      TreeNode root = new TreeNode("15");
      root.insert(t1);
      root.insert(t2);
      tree.putRoot(root);
      tree.writeToFile(1);
    }

    public static void t3(){
      Tree tree = new Tree();
      TreeNode[] basenodes = new TreeNode[4];
      String[] values = new String[]{"1,3,5", "13", "17,19,21", "25,27,29"};
      int[][] children = new int[][]{{1,3,5,7}, {13,15}, {17,19,21,23},{25,27,29, 31}};
      for(int i=0; i<4; i++){
        TreeNode node = new TreeNode(values[i]);
        for(int j=0; j<children[i].length; j++){
          node.insert(children[i][j]);
        }
        basenodes[i] = node;
      }
      TreeNode t1 = new TreeNode("7");
      t1.insert(basenodes[0]);
      t1.insert(basenodes[1]);
      TreeNode t2 = new TreeNode("23");
      t2.insert(basenodes[2]);
      t2.insert(basenodes[3]);
      TreeNode root = new TreeNode("15");
      root.insert(t1);
      root.insert(t2);
      tree.putRoot(root);
      tree.writeToFile(2);
    }

    public static void t4(){
      Tree tree = new Tree();
      TreeNode[] basenodes = new TreeNode[4];
      String[] values = new String[]{"1,3", "13", "17,19,21", "25,27,29"};
      int[][] children = new int[][]{{1,3,5}, {7,15}, {17,19,21,23},{25,27,29, 31}};
      for(int i=0; i<4; i++){
        TreeNode node = new TreeNode(values[i]);
        for(int j=0; j<children[i].length; j++){
          node.insert(children[i][j]);
        }
        basenodes[i] = node;
      }
      TreeNode t1 = new TreeNode("7");
      t1.insert(basenodes[0]);
      t1.insert(basenodes[1]);
      TreeNode t2 = new TreeNode("23");
      t2.insert(basenodes[2]);
      t2.insert(basenodes[3]);
      TreeNode root = new TreeNode("15");
      root.insert(t1);
      root.insert(t2);
      tree.putRoot(root);
      tree.writeToFile(3);
    }

    public static void t5(){
      Tree tree = new Tree();
      TreeNode[] basenodes = new TreeNode[4];
      String[] values = new String[]{"1,3", "13", "19,21", "25,27,29"};
      int[][] children = new int[][]{{1,3,5}, {7,15}, {19,21,23},{25,27,29, 31}};
      for(int i=0; i<4; i++){
        TreeNode node = new TreeNode(values[i]);
        for(int j=0; j<children[i].length; j++){
          node.insert(children[i][j]);
        }
        basenodes[i] = node;
      }
      TreeNode t1 = new TreeNode("7");
      t1.insert(basenodes[0]);
      t1.insert(basenodes[1]);
      TreeNode t2 = new TreeNode("23");
      t2.insert(basenodes[2]);
      t2.insert(basenodes[3]);
      TreeNode root = new TreeNode("15");
      root.insert(t1);
      root.insert(t2);
      tree.putRoot(root);
      tree.writeToFile(4);
    }

}