# Write a function called print_pattern that takes integer number as an argument
# and prints following pattern if input number is 3,

def print_pattern(num=5):
    for i in range(num):
        for j in range(num-i):
            print("*", end="")

        print()

user_input = input("Enter a range number:")

if user_input:
    print_pattern(int(user_input))
else:
    print_pattern()
