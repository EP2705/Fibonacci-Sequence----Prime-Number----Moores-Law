# CS1026a 2023
# Assignment 01 Project 01 - Part A
# Eliandro Pizzonia
# october 6 2023

print("Project One (01) - part A : Fibonacci Sequence")

# Getting user input for which number the sequence ends (including negatives)
end_of_sequence = abs(int(input("Sequence ends at: ")))


# Defining a function to calculate the Fibonacci number at a certain position
def fibonacci(x):

    # starting the fibonacci sequence with 0 at position 0
    if x == 0:
        return 0

    # starting the fibonacci sequence with 1 at position 1
    elif x == 1:
        return 1

    else:

        # For x values greater than 1, "a" and "b" are set to the first two numbers of the fibonacci sequence
        a, b = 0, 1

        # for loop to run from the third number of the sequence to the last number "x"
        for num in range(2, x + 1):

            # The next number of the sequence is the sun of "a" and "b"
            c = a + b

            # Updating the values of "a" and "b"
            a = b
            b = c

        # returning "b" which holds the Fibonacci number at the position of "x"
        return b


# for loop the range from 0 to the users end position
for i in range(end_of_sequence + 1):

    # Printing the position in the sequence, Fibonacci number at that position,
    # and a formatted Fibonacci number with commas
    print(str(i) + ":  " + str(fibonacci(i)) + " " + str(format(fibonacci(i), ',')))

print("\nEND: Project One (01) - Part A")
print("Eliandro Pizzonia epizzoni 251363956")
