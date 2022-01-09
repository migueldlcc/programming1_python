import java.util.Scanner;
public class StringComparison 
{
    /**
     * A class that reads three strings and sorts them lexicographically.
     * This was exercise P3.16 from Big Java: Late Objects.
     * @author: Miguel de la Cruz Cabello
     * @version: 01/24/2020
     */
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Please enter three strings: ");

        String a = in.next();
        String b = in.next();
        String c = in.next();

        if (a.compareTo(b) < 0 && a.compareTo(c) < 0)
        {
            System.out.println(a);
            if (b.compareTo(c) < 0)
            {
                System.out.println(b);
                System.out.println(c);
            }
            else 
            {
                System.out.println(c);
                System.out.println(b);
            }
        }
        
        else if (a.compareTo(b) < 0 && a.compareTo(c) > 0)
        {
            System.out.println(c);
            if (a.compareTo(b) < 0)
            {
                System.out.println(a);
                System.out.println(b);
            }
            else
            {
                System.out.println(b);
                System.out.println(a);
            }
        }
        else if (a.compareTo(b) > 0 && a.compareTo(c) > 0)
        {
            if (b.compareTo(c) < 0)
            {
                System.out.println(b);
                System.out.println(c);
                System.out.println(a);
            }
            else
            {
                System.out.println(c);
                System.out.println(b);
                System.out.println(a);
            }
        }
       
        else 
        {
            System.out.println(b);
            if (a.compareTo(c) < 0)
            {
                System.out.println(a);
                System.out.println(c);
            }
            else
            {
                System.out.println(c);
                System.out.println(a);
            }
        }
        System.out.println();  
    }


}