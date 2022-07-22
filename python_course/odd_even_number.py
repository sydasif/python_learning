# Find Odd and Even number
num = input("Enter a number to find Odd & Even number: ")
mod = int(num) % 2

# if statement is true it will run first statement else second statement
if mod > 0:
    print("This is and Odd number.")
else:
    print("This is an Even number.")
