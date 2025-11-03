# recursive function for adding all numbers until n
def recursiveAddition(n):
    # if n cannot be less than 1, so any value below it will be 0
    if n <= 0:
        # return 0 for addition
        return 0
    # return n and the sum of all recursive additions until n-1
    return n + recursiveAddition(n - 1)

# while loop to continuously receive input until 'Exit' received
while True:
    # receive input string
    num = input("Enter a number (Enter 'Exit' to quit): ")
    # if 'Exit' received as input, exit loop
    if num == "Exit":
        break

    # Check to make sure the inputted string is a digit 
    if not num.isdigit():
        # if not, print error message and go to next loop
        print("Error! Please enter a digit value only!")
        continue

    # since we should calculate the sum of all numbers before the inserted number
    # call the recursiveAddition function on n - 1
    sum = recursiveAddition(int(num) - 1)
    # print sum
    print(sum)