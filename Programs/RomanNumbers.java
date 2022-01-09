import java.util.Scanner;
public class RomanNumbers
{
    /**
     * A class that converts positive integers into the Roman number system.
     * This was exercise P3.26 from Big Java: Late Objects
     * I chose to use arrays because my first idea was to put all the letters in different lists 
     * like we used to do in python because it was the only way it came to my mind. I knew a little bit about arrays because during Christmas Break
     * my uncle gave me some "lessons" on the principles of java so I could be a little more prepared. He told me to use Oracle documetation and go to
     * the section of Java Documentation to look for doubts, like the Python Documentation we used. I also looked ahead to Capter 6 in the book for the
     * of the use of arrays. So arrays are structures that contain data (like the group of letters),
     * and are basically used to store and organize the elements inside of them, like the lists in python.
     * @author: Miguel de la Cruz Cabello
     * @version: 01/26/2020
     */
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Please enter a number: ");
        String units[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        String tens[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"}; 
        String hundreds[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        String thousands[] = {"", "M", "MM", "MMM"};
        
        int number = in.nextInt();
        int th = number / 1000;
        int h=(number / 100) % 10;
        int t= (number / 10) % 10; 
        int u= number % 10;

        if (number < 1 || number > 3999)
        {
            System.out.println("Error: Invalid value for a roman number");
        }
        
        else if (number >= 1000)
        {
            System.out.println( thousands[th] + hundreds[h] + tens[t] + units[u]);
        }
        else if (number < 1000 && number >= 100)
        {
            System.out.println(hundreds[h] + tens[t]+ units[u]);
        }
        else if ( number < 100 && number >= 10)
        {
            System.out.println(tens[t] + units[u]);
        }
        else 
        {
            System.out.println(units[u]);
        }
    }
}