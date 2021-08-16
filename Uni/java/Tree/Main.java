public class Main {

    public static void main(String[] args) {
     
      /*int inserts[][] = new int[][]{{5,2,9,1,3,8,4},{8,5,9,2,1,3,4},{3,2,8,1,5,9,4},{7,3,8,2,5,9,1,4},{2,1,7,5,8,4,9}};
      for(int i=0; i<inserts.length; i++){
        Tree tree = new Tree();
        for(int j=0; j<inserts[i].length; j++){
          tree.insert(inserts[i][j]);
        }
        tree.writeToFile(i);
      }*/

      /*Tree tree = new Tree();
      int k = 64;
      tree.insert(k);
      for(int i=0; i<5; i++){
        int begin = k/2;
        if(i!=4){
          for(int j=0; j<Math.pow(2, i+1); j++){
            tree.insert(begin+j*k);
          }
          k = begin;
        }else{
          tree.insert(begin);
        }
        
      }
      tree.writeToFile(1);*/
      /*
      int inserts[] = new int[]{64,32,96,16,48,80,112,8,24,40,72,88,104,120,2,92,108,116,124,126};
      Tree tree = new Tree();
      for(int i=0; i<inserts.length; i++){
        tree.insert(inserts[i]);
      }
      tree.writeToFile(1);*/

      int inserts[] = new int[]{3,2,5,1,4,8,9};
      Tree tree = new Tree();
      for(int i=0; i<inserts.length; i++){
        tree.insert(inserts[i]);
      }
      tree.writeToFile(1);
    }

}