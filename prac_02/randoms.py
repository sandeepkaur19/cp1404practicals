import random
print(random.randint(5, 20))            # line 1
print(random.randrange(3, 10, 2))       # line 2
print(random.uniform(2.5, 5.5))         # line 3

# 1 The code prints a random number. The smallest number you could see is 5 and the largest is 20
# 2 It prints a random odd number. Smallest number is 3 and largest is 9. It could not produce a 4
# 3 It printed a random decimal. Smallest number is 2.5 and largest is 5.5

print(random.randint(1,100))