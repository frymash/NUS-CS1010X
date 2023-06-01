import java.util.Scanner;
import java.util.ArrayList;

public class TowerOfHanoi_ans {
  String name;
  ArrayList[] peg;
  int numDiscs;

  public TowerOfHanoi_ans(String name, int n) {
    this.name = name;
    this.numDiscs = n;
    this.peg = new ArrayList[3];
    // Write your code here
    for (int i = 0; i < 3; i++) {
      this.peg[i] = new ArrayList();
    }
    for (int i = 0; i < n; i++) {
      this.peg[0].add(i);
    }
  }

  private void moveDisc(int src, int des) {
    // Write your code here
    int disc = (int) peg[src].remove(peg[src].size() - 1);
    peg[des].add(disc);
    printTower();
  }

  public void printTower() {
    // Write your code here
    // Curly brackets are only needed when they contain more than
    // one statement
    for (int i = 0; i < 3; ++i) {
      System.out.print("[");
      for (int j = 0; j < peg[i].size(); ++j) {
        System.out.print(" " + peg[i].get(j));
      }

      System.out.print(" ]");
      if (i < 2) {
        System.out.print(", ");
      }
    }
    System.out.println();
  }

  public void makeMoves(int n, int src, int des, int aux) {
    if (n <= 0) return;
    makeMoves(n-1, src, aux, des);
    moveDisc(src, des);
    makeMoves(n-1, aux, des, src);
    return;
  }
  
  public static void main(String args[]) {
    Scanner input = new Scanner(System.in);
    System.out.println("Enter number of disks: ");
    int n = input.nextInt();
    TowerOfHanoi_ans t = new TowerOfHanoi_ans("Hanoi", n);
    t.printTower();
    t.makeMoves( n, 0, 2, 1 );
  }
  
}
  