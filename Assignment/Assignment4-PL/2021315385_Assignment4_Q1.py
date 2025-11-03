# RandomStats.py application
import random

# list to store 200 random values
numbers = []
# Counter list
counter = [0] * 5

# generating 200 random values between 1 and 100
for _ in range (200):
    # generate a random value between 1 and 100
    num = random.randint(1,100)
    
    # increment counter based on range
    if 1 <= num <= 20:
        counter[0] += 1
    elif 21 <= num <= 40:
        counter[1] += 1
    elif 41 <= num <= 60:
        counter[2] += 1
    elif 61 <= num <= 80:
        counter[3] += 1
    else:
        counter[4] += 1

    # append value to numbers list
    numbers.append(num)

# sort values of list
numbers.sort()

# for loop to print 20 values in each line
# for loop has a step of 20
for i in range(0, 200, 20):
    #print the values using the requested format
    print(' '.join(f"{n:3}" for n in numbers[i:i + 20]))

# format printing
print('-' * 37)

# formatted printing of the star graph
for i in range(5):
    print("{0:2} - {1:3}: {2}\t{3}".format(i * 20 + 1, (i + 1) * 20, '*' * counter[i], counter[i]))