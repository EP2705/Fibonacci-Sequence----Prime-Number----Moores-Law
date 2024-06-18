# CS1026a 2023
# Assignment 01 Project 01 - Part B
# Eliandro Pizzonia
# 251363956
# epizzoni
# october 6 2023

print("Project One - Part B: Prime Choice")

# Getting user input for the starting number and the ending number for the range of prime numbers
start_num = int(input("\nPrime Numbers starting with: "))
end_num = int(input("and ending with: "))

# if statement in case the starting number is greater than ending number
if start_num > end_num:

    # variables are flipped if the starting number is greater than ending number
    print("\nIncorrect Input: " + str(start_num) + " is greater than " + str(
        end_num) + "\nThe numbers have been automatically switched.")

    end_num, start_num = start_num, end_num

# Printing the range of prime numbers
print("\nPrime numbers in the range from: " + str(start_num) + " and " + str(end_num) + " are: ")

# if statement in case the starting number is less then or equal to 1 (set to the lowest prime: 2)
if start_num <= 1:
    start_num = 2

# for loop to loop through the range of numbers
for i in range(start_num, end_num + 1):
    divisible = 0

    # Checking if "i" is prime by dividing it by the numbers from the range of 2 to (i-1)
    for num in range(2, i):
        if i % num == 0:

            # if "i" is divisible by any of the numbers, the divisible count is set to one
            divisible = 1

    # If the divisible count is equal to 0, "i" is prime
    if divisible == 0:

        # printing the prime numbers
        print(str(i) + " is prime")


print("\nEnd Project One (01) - Part B")
print("Eliandro Pizzonia epizzoni 251363956")
