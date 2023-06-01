import java.util.*;

public class VehiclePlate {
   public static char generateCheckSum(String prefix, int suffix) {
      char[] letters = {'A', 'Z', 'Y', 'X', 'U', 'T', 'S',
                        'R', 'P', 'M', 'L', 'K', 'J', 'H', 
                        'G', 'E', 'D', 'C', 'B'};
      List<Integer> numbers = new ArrayList<Integer>();
      char[] prefix_letters = prefix.toCharArray();
      
      int start = 0;
      
      if (prefix.length() == 3) {
         start = 1;
      } else if (prefix.length() == 1) {
         numbers.add(0);
      }
      
      // Convert prefix letters to numbers and add to numbers list
      for (int i = start; i < prefix_letters.length; i++) {
         char prefix_letter = prefix_letters[i];
         int char_pos = prefix_letter - 'A'+ 1;
         numbers.add(char_pos);
      }
      
      // Push numbers from the plate onto a stack in reverse orders
      // and pad with 0s wherever necessary
      LinkedList<Integer> stack = new LinkedList<Integer>();
      int to_add = 0;
      int ideal_stack_size = 4;
      while (suffix != 0) {
         to_add = suffix % 10;
         stack.push(to_add);
         suffix = suffix / 10;
         // System.out.println(to_add);
      }
      while (stack.size() < ideal_stack_size) {
         stack.push(0);
      }

      // System.out.println(stack);
      
      // Pop the numbers from the stack and add them to the numbers list
      while (stack.size() > 0) {
         to_add = stack.pop();
         numbers.add(to_add);
      }
      
      // System.out.println("Numbers before multiplication:");
      // System.out.println(numbers);

      // Generate final numbers list and find the number list sum + remainder
      List<Integer> multipliers = new ArrayList<Integer>();
      Collections.addAll(multipliers,9,4,5,4,3,2);
      int sum = 0;
      int remainder = 0;
      for (int i = 0; i < numbers.size(); i++) {
         numbers.set(i, numbers.get(i) * multipliers.get(i));
         sum = sum + numbers.get(i);
      }

      remainder = sum % 19;

      return letters[remainder];
   }

   public static void main(String[] args) {

      Scanner sc = new Scanner(System.in);
      System.out.println("Vehicle Plate (excluding the checksum alphabet at the end):");
      String plate = sc.nextLine().toUpperCase();
      String prefix = plate.replaceAll("[0123456789]", "");
      int suffix = Integer.parseInt(plate.replaceAll("[a-zA-z]", ""));
      char checksum = generateCheckSum(prefix, suffix);
      System.out.println("Vehicle Plate is: " + prefix + " " + suffix + " " + checksum);

   } // end main

}// end class 