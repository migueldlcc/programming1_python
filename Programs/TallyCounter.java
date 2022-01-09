public class TallyCounter
{
    // Instance variables
    // Defines a variable with a type and name
    private int value;
    // Every instance wariable wil be "private"
    // Private things cannot be sen by users of the class
    // Public things can....

    // Constructor
    // It is a special method that *sets up the instance variables*
    // We will always have a constructor
    // The constructor always has a capital letter at the start, because its name always matches the class name
    public TallyCounter()
    {
        // Set up the variable(s)
        value = 0;
        // Do not type "int value = 0"
    }

    // Instance methods

    // Mutator - sometimes we need a return value, often we don't
    // Accessor

    // Instance variables will be private
    // Methods might be public or private, the public ones are meant for users to call
    // All the public methods together form the "public INTERFACE" to the object/class
    /**
     * Increments the counter by one.
     */
    public void count()
    {
        value ++;
    }

    /**
     * Resests the counter to zero.
     */
    public void clear()
    {
        value = 0;
    }

    /**
     * Get the current value of the counter.
     * 
     * @return: the current value
     */
    public int getValue()
    {
        return value;
    }
}