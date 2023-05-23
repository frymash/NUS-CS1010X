public class rec11 {
    public static int fib(int n) {
        switch (n) {
            case 0:
                return 0;
            case 1:
                return 1;
            default:
                int prev = 0;
                int curr = 1;
                int result = 0;
                for (int i = 2; i <= n; i++) {
                    result = prev + curr;
                    prev = curr;
                    curr = result;
                }
        return result;
        }
    }

    public static void main(String[] args) {
        int max = 47;
        for (int i = 0; i <= max; i++) {
            System.out.printf("fib(%d) | %d%n", i, fib(i));
        }
    }
}