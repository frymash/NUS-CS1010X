public class ArraySplit {
  // print_arr
  private static void print_arr(int arr[]) {
    int i = 0;
    while (i < arr.length && arr[i] != Integer.MIN_VALUE) {
      System.out.printf("%d  ", arr[i]);
      i++;
    }
    System.out.println();
 }

 // split_array
 private static void split_array(int input[], int n, int left[], int right[]) {
    // Initialise output arrays

    for (int i = 0; i < left.length; i++){
      left[i] = Integer.MIN_VALUE;
      right[i] = Integer.MIN_VALUE;
    }
    int l_cnt = 0;
    int r_cnt = 0;
    for (int i=0; i < input.length; i++) {
      if (input[i] <= n){
        left[l_cnt] = input[i];
        l_cnt++;
      }
      else {
        right[r_cnt] = input[i];
        r_cnt++;
      } 
    }
    return;
  }
  
  // main function
  public static void main (String [] args) {
    int[] input = {12,8,3,4,10, 1,0,2,7,9,3,4,5};

    int[] left = new int[input.length];
    int[] right = new int[input.length];
    //split_array(input, 13, left, right); // to make sure right is empty
    //split_array(input, -10, left, right); // to make sure left is empty
    //split_array(input, 6, left, right); // to make sure left and right are okay
    split_array(input, 7, left, right); // to make sure left and right are okay even with number in the array
    

    System.out.println("input array values: ");
    print_arr(input);
    
    System.out.println("left array values: ");
    print_arr(left);
 
    System.out.println("right array values: ");
    print_arr(right); 
 }

} // end of class
