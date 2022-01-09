import java.util.Scanner;
public class P25
{
    /**
     * A class that prints different mathematical equations and aligns them. 
     * This was exercise P.25 from Big Java: Late Objects
     * @author: Miguel de la Cruz Cabello
     * @version: 01/17/2020
     */
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Please enter a number: ");
        double num1 = in.nextDouble();

        System.out.print("Please enter a second number: ");
        double num2 = in.nextDouble();
        
        double result1 = (double) (num1 + num2);
        double result2 = (double) (num1 - num2);
        double result3 = (double) (num1 * num2);
        double result4 = (double) (result1 / 2);
        double result5 = (double) (Math.abs(num1 - num2));
        double result6 = (double) (Math.max(num1, num2));
        double result7 = (double) (Math.min(num1, num2));

        System.out.printf("Sum: %17.2f", (double) result1);
        System.out.println();
        System.out.printf("Difference: %10.2f", (double) result2);
        System.out.println();
        System.out.printf("Product: %13.2f", (double) result3);
        System.out.println();
        System.out.printf("Average: %13.2f", (double) result4);
        System.out.println();
        System.out.printf("Distance: %12.2f", (double) result5);
        System.out.println();
        System.out.printf("Maximun: %13.2f", (double) result6);
        System.out.println();
        System.out.printf("Minimun: %13.2f", (double) result7);
        System.out.println();
    }
}