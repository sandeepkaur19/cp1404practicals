numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0])              # 3
print(numbers[-1])             # 2
print(numbers[3])              # 1
print(numbers[:-1])            # every element until [-1] which is 2
print(numbers[3:4])            # 1
print(5 in numbers)            # true
print(7 in numbers)            # false
print("3" in numbers)          # false
print(numbers + [6, 5, 3])     # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"    # Change the first element of numbers to "ten"
print(numbers)
numbers[-1] = 1       # change the last element to 1
print(numbers)
numbers[2:]           # get all the elements from numbers except the first two
print(numbers)
print(9 in numbers)   # check if 9 is an element of numbers
