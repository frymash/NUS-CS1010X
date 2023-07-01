import java.util.*;

public class VehiclePlate {
 
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
     
      // prefix part....
      int digit[] = { 0, 0, 0, 0, 0, 0 };
      switch (prefix.length()) {
        case 3:
          digit[0] = prefix.charAt(1) - 'A' + 1;
          digit[1] = prefix.charAt(2) - 'A' + 1;
          break;
        case 2:
          digit[0] = prefix.charAt(0) - 'A' + 1;
          digit[1] = prefix.charAt(1) - 'A' + 1;
          break;        
        case 1:
          digit[1] = prefix.charAt(0) - 'A' + 1;
          break;
        default: 
          System.out.println("Unrecognize plate: " + prefix + " " + suffix);
          return '*';
      }
      
      // suffix
      
      if (suffix > 9999) {
        System.out.println("Unrecognize plate: " + prefix + " " + suffix);
        return '*';
      };
      int d = 5;    
      while (suffix > 0) {
        digit[d] = suffix%10; suffix /= 10;
        d -= 1;
      };
     
      // calculation
      int multipler[] = { 9, 4, 5, 4, 3, 2};
      int sum = 0;
      for (int i = 0; i < 6; i++) 
        sum += digit[i] * multipler[i];
 
      String code = "AZYXUTSRPMLKJHGEDCB";
      return code.charAt(sum%19);

   }// end generateCheckSum

}// end class 