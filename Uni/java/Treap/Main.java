public class Main {

    public static void main(String[] args) {

      Tree tree = new Tree();
      tree.insert(5, 5, "Gute");
      tree.insert(3, 17, "Gotland");
      tree.insert(2, 23, "Brillen");
      tree.insert(4, 28, "Charollais");
      tree.insert(7, 55, "Texel");
      tree.insert(6, 12, "Rhön");
      tree.insert(8, 10, "Rhön");
      tree.writeToFile(0);

      tree = new Tree();
      tree.insert(5, 5, "Gute");
      tree.insert(3, 17, "Gotland");
      tree.insert(2, 23, "Brillen");
      tree.insert(4, 28, "Charollais");
      tree.insert(7, 10, "Rhön");
      tree.insert(6, 12, "Rhön");
  
      tree.writeToFile(1);


      tree = new Tree();
      tree.insert(5, 10, "Gute");
      tree.insert(3, 17, "Gotland");
      tree.insert(2, 23, "Brillen");
      tree.insert(4, 28, "Charollais");
      tree.insert(7, 12, "Texel");
      tree.writeToFile(2);

      tree = new Tree();
      tree.insert(5, 12, "Gute");
      tree.insert(3, 17, "Gotland");
      tree.insert(2, 23, "Brillen");
      tree.insert(7, 28, "Texel");
      tree.writeToFile(3);


    }

}