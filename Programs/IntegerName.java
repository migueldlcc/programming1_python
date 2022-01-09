/**
 * Work Cited:
 * I used the code source from the book that was in the webpage
 * For P5.13 I found the method .trim() in https://www.geeksforgeeks.org/trim-remove-leading-trailing-spaces-string-java/ which 
 * consists in eliminate the leading spaces
 */
import java.util.Scanner;

/**
 * A class that turns an integer into its English name.
 * This were exercises P5.11, P5.12, and P5.13 from Big Java: Late Objects.
 * @author: Miguel de la Cruz Cabello
 * @version: 02/01/2020
 */
public class IntegerName
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Please enter any positive or negative integer smaller than 1000000000: ");
        int input = in.nextInt();
        System.out.println(intName(input));
        in.close();
    }


    /**
     * A class that converts a number into its English name.
     * @param number
     * @return the name of the number in letters
     */
    public static String intName(int number)
    {
        int part = number;
        String name = "";

        if (part == 0) 
        {
            return "zero";
        }
        if (part < 0)
        {
            part = part * (-1);
            return "minus " + intName(part);
        }

        if (part >= 100000000)
        {
            if (part / 1000000 % 100 == 0)
            {
                name = digitName(part / 100000000) + " hundred million";
                part = part % 100000000;
            }
            else
            {
                name = digitName(part / 100000000) + " hundred";
                part = part % 100000000;
            }
        }

        if (part >= 1000000) 
        {
            if (part >= 20000000 && part < 100000000)
            {
                name = name + " " + tensName(part / 1000000) + " " + digitName(part / 1000000 % 10) + " million";
                part = part % 1000000; 
            }
            else if ( number >= 10000000 && part < 20000000)
            {
                name = name + " " + teenName(part / 1000000) + " million";
                part = part % 1000000;
            }
            else if ( part >= 1000000 && part < 10000000)
            {
                name = name + " " + digitName(part / 1000000) + " million";
                part = part % 1000000;
            }
        }

        if (part >= 100000)
        {
            if (part / 1000 % 100 == 0)
            {
                name = name + " " + digitName(part / 100000) + " hundred thousand";
                part = part % 100000;
            }
            else
            {
                name = name + " " + digitName(part / 100000) + " hundred";
                part = part % 100000;
            }
        }


        if (part >= 1000)
        {
            if (part >= 20000 && part < 100000)
            {
                name = name + " " + tensName(part / 1000) + " " + digitName(part / 1000 % 10) + " thousand";
                part = part % 1000;
            }
            else if (part >= 10000 && part < 200000)
            {
                name = name + " " + teenName(part / 1000) + " thousand";
                part = part % 1000;
            }
            else if (part >= 1000 && part < 10000)
            {
                name = name + " " + digitName(part / 1000) + " thousand";
                part = part % 1000; 
            }
        }

        if (part >= 100)
        {
            name = name + " " + digitName(part / 100) + " hundred";
            part = part % 100;
        }

        if (part >= 20)
        {
            name = name + " " + tensName(part);
            part = part % 10;
        }
        else if (part >= 10)
        {
            name = name + " " + teenName(part);
            part = 0;
        }

        if (part > 0)
        {
            name = name + " " + digitName(part);
        }
        return name.trim();
    
    }

    

    /**
    * A class that converts digit into its English name.
    * @param digit an integer between 1 and 9
    * @return the name of digit in letters
    */
   public static String digitName(int digit)
   { 
      if (digit == 1) { return "one"; }
      if (digit == 2) { return "two"; }
      if (digit == 3) { return "three"; }
      if (digit == 4) { return "four"; }
      if (digit == 5) { return "five"; }
      if (digit == 6) { return "six"; }
      if (digit == 7) { return "seven"; }
      if (digit == 8) { return "eight"; }
      if (digit == 9) { return "nine"; }
      return "";
   }

    /**
    * A class that converts a "teen" number into its English name.
    * @param number an integer between 10 and 19
    * @return the name of the "teen" number in letters
    */
   public static String teenName(int number)
   {  
      if (number == 10) { return "ten"; }
      if (number == 11) { return "eleven"; }
      if (number == 12) { return "twelve"; }
      if (number == 13) { return "thirteen"; }
      if (number == 14) { return "fourteen"; }
      if (number == 15) { return "fifteen"; }
      if (number == 16) { return "sixteen"; }
      if (number == 17) { return "seventeen"; }
      if (number == 18) { return "eighteen"; }
      if (number == 19) { return "nineteen"; }
      return "";
   }

    /**
    * A class that converts the tens into their English name.
    * @param number an integer between 20 and 99
    * @return the name of the tens in letters
    */
   public static String tensName(int number)
   {   
      if (number >= 90) { return "ninety"; }
      if (number >= 80) { return "eighty"; }
      if (number >= 70) { return "seventy"; }
      if (number >= 60) { return "sixty"; }
      if (number >= 50) { return "fifty"; }
      if (number >= 40) { return "forty"; }
      if (number >= 30) { return "thirty"; }
      if (number >= 20) { return "twenty"; }
      return "";
   }
}
