# Average Calculator Algorithm using a counter

# Ask the user to enter how many numbers they want to average

n = int(input("Enter number of values: "))

# Initialize sum and counter variables

sum = 0

# start counter at 1 
counter = 1

# Loop until the counter exceeds n
while counter <= n:
    # Ask the user to enter a number
    number = float(input("Enter number:"))
   
   # Add the number to sum
    sum = sum + number
   
   # Increase the counter
    counter = counter + 1

# Calculate the average
average = sum/n

# Display the result
print(f" The average of {n} numbers is {average}.")