import java.util.Scanner;

public class lecture_14 {
    public static void swap1 (int a, int b) {
        int temp = a;
        a = b;
        b = temp;
        System.out.println(a + " " +  b);
    }
    public static void main (String[] args) {
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();
        char character = input.next().charAt(1);
        String string = input.nextLine();
        System.out.println(number + "'" + character + " is" + string);
        swap1(4,6);
    }
}