import sys
import random

n = 1000
maxint = 1e9

print(n)

for i in range(n):
    sys.stdout.write(str(random.randint(0, maxint)) + " ")

sys.stdout.write("\n")

for i in range(n):
    sys.stdout.write(str(random.randint(0, maxint)) + " ")

sys.stdout.write("\n")

for i in range(n):
    sys.stdout.write(str(random.randint(0, maxint)) + " ")

sys.stdout.write("\n")
