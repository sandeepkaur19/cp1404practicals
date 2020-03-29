# Program 1
name_file = open("name.txt", "w")
name = input("what is your name?")
print(name, file=name_file)
name_file.close()

# Program 2
name_file = open("name.txt", "r")
name = name_file.read()
print("your name is", name)

# Program 3
number_file = open("numbers.txt", "r")
first_number = int(number_file.readline())
second_number = int(number_file.readline())
number_file.close()
print(first_number + second_number)

# Program 4
number_file = open("numbers.txt", "r")
total = 0
for line in number_file:
    number = int(line)
    total += number
number_file.close()
print(total)
