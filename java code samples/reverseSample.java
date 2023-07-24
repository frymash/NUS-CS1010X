import java.util.Arrays;

public class reverseSample {
    public static void reverse(int[] xs) {
        int front = 0;
        int back = xs.length-1;
        while (front < back) {
            int temp = xs[front];
            xs[front] = xs[back];
            xs[back] = temp;
            front++;
            back--;
        }
    }
    
    public static void main(String[] args) {
        int[] lst1 = {5,4,3,2,1};
        int[] lst2 = {11,10,9,8,7,6};
        reverse(lst1);
        reverse(lst2);
        System.out.println(Arrays.toString(lst1));
        System.out.println(Arrays.toString(lst2));
    }
}