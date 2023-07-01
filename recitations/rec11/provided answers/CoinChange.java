import java.util.Scanner;

public class CoinChange {
    private static int cc(int amount, int kinds_of_coins) {
        if (amount < 0 || kinds_of_coins <= 0) {
            return 0;
        } else if (amount == 0) {
            return 1;
        } else {
            return cc(amount, kinds_of_coins - 1)
                + cc(amount - first_denomination(kinds_of_coins),
                    kinds_of_coins);
        }
    }

    private static int first_denomination(int kinds_of_coins) {
        int[] coins = {1,5,10,20,50};
        //int[] coins = {50, 20, 10, 5, 1};
        return coins[kinds_of_coins - 1];
    }
    
    public static void main(String [] args) {
        int user_amt;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter amount in cents: ");
        user_amt = input.nextInt();
        System.out.printf("There are %d ways to form change for %d cents.\n", 
            cc(user_amt, 5), user_amt);  
    }
}
