# function to check if number is Prime
def isPrime(n):
    # any value below 2 is not a prime number
    if n < 2:
        return False
    # 2 is a prime number
    elif n == 2:
        return True
    
    # even numbers are not prime
    if n % 2 == 0:
        return False
    
    # is prime number if n has an odd numbered factor less than the square root of n
    # 3 = smallest odd number after 1
    i = 3
    # check to make sure i is less than or equal to the square root of n
    while i ** 2 <= n:
        # if n has a factor of i, not prime
        if n % i == 0:
            return False
        # move on to next odd number
        i += 2
    
    return True

# finds the prime number at rank n
def primeChecker(n):
    # counter for the prime rank
    counter = 0
    # current number value
    num = 1
    # continuous while loop
    while True:
        # check if number is Prime
        if isPrime(num):
            # if prime, increase counter
            counter += 1
            # if current prime number is the requested rank, return num
            if counter == n:
                return num
        # increment number
        num += 1

# infinite loop to receive input
while True:
    # input
    prime = input("What is the prime number at rank: ")

    # Check to make sure the inputted string is a digit 
    if not prime.isdigit():
        # if not, print error message and go to next loop
        print("Error! Please enter a digit value only!")
        continue

    # convert to int
    prime = int(prime)

    # check if input is a positive number
    if prime <= 0:
        # if not, print error message and go to next loop
        print("Error! Please enter a positive value only!")
        continue

    # print result in requested format
    print("The prime number is {0}\n".format(primeChecker(prime)))
    