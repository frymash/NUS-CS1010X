//quicksort

public class QuickSort {
  private static void print_arr(int arr[]) {
    int i = 0;
    while (i < arr.length && arr[i] != Integer.MIN_VALUE) {
      System.out.printf("%d  ", arr[i]);
      i++;
    }
    System.out.println();
 }

 private static void split_array(int input[], int start, int end, int n, int left[], int right[]) {
    // Initialise output arrays
    int len = end - start + 1;
    if (len < 1) return;
    
    //System.out.println("len: " + len);
    for (int i = 0; i < left.length; i++){
      left[i] = Integer.MIN_VALUE;
      right[i] = Integer.MIN_VALUE;
    }
    int l_cnt = 0;
    int r_cnt = 0;
    for (int i=0; i < len; i++) {
      if (input[start+i] <= n){
        left[l_cnt] = input[start+i];
        l_cnt++;
      }
      else {
        right[r_cnt] = input[start+i];
        r_cnt++;
      } 
    }
    return;
  }
  
 
  public static void helper_sort(int[] input, int start, int end) {     
     if (start >= end) {
        return;
     }
     
     int[] left = new int[end-start+1];
     int[] right = new int[end-start+1];
     System.out.println("before...");
     int splitter = input[start];
     split_array(input, start+1, end, splitter, left, right);
     // put back to input
     int cnt = 0;
     for (int i=0; i < left.length; i++){
         if (left[i] == Integer.MIN_VALUE)
             break;
         input[start+cnt] = left[cnt];
         cnt += 1;
     }
     //System.out.println("splitter " + splitter + "  left length: " + cnt);
     input[start+cnt] = splitter;
     int cnt2;
     cnt2 = 0;
     for (int i=0; i < right.length; i++) {
         if (right[i] == Integer.MIN_VALUE)
             break;
         input[start+cnt+1+cnt2] = right[i];
         cnt2 += 1;
     }
     //System.out.println("splitter " + splitter + "  right length: " + (cnt2-1));
     //System.out.println("after...");
     //print_arr(left);
     //print_arr(right);
     print_arr(input);
     
     // recursion
     System.out.println("recursion..." + "start:" + start + "   start+cnt-1:" + (start+cnt-1) + " start+cnt+1: " + (start+cnt+1) + "  end-1:" + (end-1));;
     helper_sort(input, start, start+cnt-1);
     helper_sort(input, start+cnt+1, end);
  }
 
  public static void sort(int[] input) {
      // call the recursive version
      helper_sort(input, 0, input.length-1);
  }
 
  public static void main (String [] args) {
    int[] input = {6,12,8,3,4,10, 1,0,2,7,9,3,4,5};

    /* 
    int[] left = new int[input.length];
    int[] right = new int[input.length];
    split_array(input, 0, input.length-1, 7, left, right);
    System.out.println("input array values: ");
    print_arr(input);
    System.out.println("left array values: ");
    print_arr(left);
    System.out.println("right array values: ");
    print_arr(right); */
    
    System.out.println("sorting...");
    sort(input);
    print_arr(input);
  }
}
