// import java.lang.Math;

public class CircleArea {
    
    public static double calculateArea(double side) {
        // double half_side = side/2;
        double radius_sq = 2 * side/2 * side/2;
        System.out.printf("Radius squared: %f\n", radius_sq);
        double result = Math.PI * radius_sq;
        return result;
    }
    public static void main(String[] args) {
        System.out.printf("%.16f\n", calculateArea(1.41421356237));
    }
}