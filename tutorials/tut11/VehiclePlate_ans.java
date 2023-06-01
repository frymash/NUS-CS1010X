import java.util.*;

public class VehiclePlate_ans {
 
   public static void main(String[] args) {

      Scanner stdIn = new Scanner(System.in);

      System.out.print("Vehicle Plate (excluding the checksum alphabet at the end): ");
      String plate = stdIn.nextLine();
      plate = plate.toUpperCase();
      String prefix =  plate.replaceAll("[0123456789]", "");
      int suffix = Integer.parseInt(plate.replaceAll("[a-zA-Z]",""));
      char checkSum = generateCheckSum (prefix, suffix);

      System.out.println("Vehicle Plate is: " + prefix + " " + suffix + " " + checkSum);

   } // end main

   /*********************************************************
      
   **********************************************************/

   public static char generateCheckSum(String prefix, int suffix) {
      int[] digit = {0,0,0,0,0,0};
      // int[] digit = new int[6];

      // prefix
      switch (prefix.length()) {
         case 1:
            digit[1] = prefix.charAt(0) - 'A' + 1;
            break;
         case 2:
            digit[0] = prefix.charAt(0) - 'A' + 1;
            digit[1] = prefix.charAt(1) - 'A' + 1;
            break;
         case 3:
            digit[0] = prefix.charAt(1) - 'A' + 1;
            digit[1] = prefix.charAt(2) - 'A' + 1;
            break;
      }

      // suffix
      int d = 5;
      while (suffix > 0) {
         digit[d--] = suffix % 10;
         suffix /= 10;
      }

      // calculation
      int[] mul = {9,4,5,4,3,2};
      int sum = 0;
      for (int i = 0; i < 6; i++) {
         sum += mul[i] * digit[i];
      }

      // return the char
      String code = "AZYXUTSRPMLKJHGEDCB";
      return code.charAt(sum % 19);

   }
   // end generateCheckSum

}// end class 