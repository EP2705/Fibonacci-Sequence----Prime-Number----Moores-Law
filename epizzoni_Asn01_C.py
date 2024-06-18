# CS1026a 2023
# Assignment 01 Project 01 - Part C
# Eliandro Pizzonia
# 251363956
# epizzoni
# october 6 2023

print("Project One (01) - Part C: The Moore the Merrier")

# Getting user input for the starting number of transistors, starting year, and total number of years
transistors = int(input("Starting Number of transistors: "))
starting_year = int(input("Starting Year: "))
total_years = int(input("Total Number of Years: "))

# Adding the starting year to the total years to get the ending year
starting_year_2 = starting_year + total_years

# printing the header
print("\nYEAR : Transistors : Flops: ")

# Defining variables for the unit and unit type
unit = 0
unit_type = ""

# for loop to loop from the starting year to the end year (increasing by every two years)
for years in range(starting_year, starting_year_2 + 1, 2):

    # calculating flops
    flops = transistors * 50

    # determining the unit type and value of the unit based on value of flops
    if flops >= (1 * 10) ** 24:
        unit = flops / (1 * 10) ** 24
        unit_type = "yottaFLOPS"

    elif flops >= (1 * 10) ** 21:
        unit = flops / (1 * 10) ** 21
        unit_type = "zettaFLOPS"

    elif flops >= (1 * 10) ** 18:
        unit = flops / (1 * 10) ** 18
        unit_types = "exaFLOPS"

    elif flops >= (1 * 10) ** 15:
        unit = flops / (1 * 10) ** 15
        unit_type = "petaFLOPS"

    elif flops >= (1 * 10) ** 12:
        unit = flops >= (1 * 10) ** 12
        unit_type = "teraLOPS"

    elif flops >= 1000000000:
        unit = flops / 1000000000
        unit_type = "gigaFLOPS"

    elif flops >= 1000000:
        unit = flops / 1000000
        unit_type = "megaFLOPS"

    elif flops >= 1000:
        unit = flops / 1000
        unit_type = "kiloFLOPS"

    elif flops < 1000:
        unit = flops
        unit_type = "FLOPS"

    # Formatting transistors and flops with commas
    formatted_transistors = "{:,}".format(transistors)
    formatted_flops = "{:,}".format(flops)

    # Printing the years, formatted transistors, unit value, unit type, and formatted flops
    print("{:<4} {:<2} {:.2f} {:<5} {:<7}".format(years, formatted_transistors, unit, unit_type, formatted_flops))

    # Doubling the number of transistors
    transistors *= 2

print("\nEND: Part One (01) - Project C")
print("Eliandro Pizzonia epizzoni 251363956")
