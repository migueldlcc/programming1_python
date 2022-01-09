public class ParcticeExam
{
    public static void main(String[] args)
    {
       double total = 0;
       while (in.hasNextDouble())
       {
           double input = in.nextDouble();
           total = total + input;
           System.out.println(total);
       }
    }
}