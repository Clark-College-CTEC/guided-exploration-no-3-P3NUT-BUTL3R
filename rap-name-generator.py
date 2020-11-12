# Guided Exploration No. 3
# Jarin Alvarez

# Import the random library
import random

# Create an empty list
possible_names = []

# Creates/opens the text files to be written to
outputFile = open('rap-names-output.txt', 'w')

# Open text file to reading
with open('rap-names.txt', 'r') as dataFile:
    # itterate through the names in the text file
    for name in dataFile:
        # append the rstripped name to the empty list
        possible_names.append(name.rstrip())

# How many times to create a rap name
count = int(input('How many rap names would you like to create? '))
# How long the name should be
parts = int(input('How many parts should the name contain? '))

# loop for the inputted number of itterations
for i in range(count):
    # create an empty list
    name_parts = []
    # loop for the inputted number of parts the name should have
    for j in range(parts):
        # choose a random number between 0 and the length of possible_names list -1, choose that element in the list, and append that element to the empty list name_parts
        name_parts.append(possible_names[random.randint(0, len(possible_names)-1)])

    # writes the name_parts list elements to the text file and joins them with a space separating each word.
    outputFile.write(f"{' '.join(name_parts)}\n")
    # print the written output into the terminal
    print(f"{' '.join(name_parts)}")

# Close the text file
outputFile.close()
