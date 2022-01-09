import java.util.Scanner;
public class IntegerComparison
{
    /**
     * A class that reads four integers and prints "two pairs" or "not two pairs" whether the input consists
     * of two matching pairs or not
     * This exercise was P3.8 from Big Java: Late Objects
     * @author: Miguel de la Cruz Cabello
     * @version: 01/24/2020
     */
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Please enter four numbers: ");
        
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();
        int d = in.nextInt();

        if (a == b && c == d || a == c && b == d || a == d && b == c)
        {
            System.out.println("Two pairs");
        }
        else
        {
            System.out.println("Not two pairs");
        }    
    }
}
