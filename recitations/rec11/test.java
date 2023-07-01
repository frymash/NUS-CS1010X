// Solutions to an exercise from mooc.fi's Java Programming course
// Part 3: Discovering errors
//
// Discussion involving this problem:
// https://www.reddit.com/r/javahelp/comments/rq1rgf/java_programming_1_course_part_3_discovering/
//
// Original problem:
// https://java-programming.mooc.fi/part-3/1-discovering-errors

import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int values = 0;
        int sum = 0;
        
        try {
            while (true) {
                System.out.println("Provide a value, a negative value ends the program");
                int value = Integer.valueOf(scanner.nextLine());
                if (value < 0) {
                    break;
                }
            
                values = values + 1;
                sum = sum + value;
            }
            System.out.println("Average of values: " + (1.0 * sum / values));
        }
        catch (Exception NumberFormatException) {
            System.out.println("The average of the values could not be calculated.");
        }
    }
}
