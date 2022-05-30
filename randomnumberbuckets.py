# random number generator and then testing that the numbers are random
import random
from collections import defaultdict

# Querying what the range of numbers is and how many numbers they'd like
low = input("What is your lowest number?\n")
int_low = int(low)

high = input("What is your highest number?\n")
int_high = int(high)

how_many = input("How many random numbers would you like?\n")
int_how_many = int(how_many)

samples = []

didget = int_low

count = defaultdict(int)

total = 0
# Creating a list from the random numbers to then calculate randomness
for _ in range(int_how_many):
    sample = random.randint(int_low, int_high)

    samples.append(sample)

# Count the random numbers and see how evenly dispersed they are
for i in samples:
    count[i] += 1
for row in count.items():
    total = sum(count.values())
    length = len(samples)
    avg = total / length
if avg == 1:
    print("This number generator is pretty random")
