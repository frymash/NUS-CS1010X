public class Fibonacci {

    private static int fib(int n) {
        int i, a = 0, b = 1;
        if (n <= 0) return a;
        if (n == 1) return b;
        for (i=2; i<=n; i++) {
            int temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }
    
    private static int fib_r(int n) {
      if (n <= 0) return 0;
      if (n==1) return 1;
      return fib_r(n-1) + fib_r(n-2);
    }
    
    public static void main(String [] args) {
        System.out.println(fib(46));
        System.out.println("recursive:" + fib_r(46));
    }
}
