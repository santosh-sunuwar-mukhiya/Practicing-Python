#Write a Python program that takes a numeric grade from the user (between 0 and 100), and prints the corresponding letter grade:
# 90–100 → A
# 80–89  → B
# 70–79  → C
# 60–69  → D
# <60    → F


def rank(score) -> str | None:
    if 100 >= score >= 90:
        return "A"
    elif 89 >= score >= 80:
        return "B"
    elif 79 >= score >= 70:
        return "C"
    elif 69 >= score >= 60:
        return "D"
    else:
        return "F"

result = True
while result:
    try:
        marks = int(input("Enter your grade between(0 - 100):"))
        if 100 < marks < 0:
            raise ValueError("Value must be greater than 0 and less than 100.")
        grade = rank(marks)
    except Exception as e:
        print(f"You got Exception '{e}'.")
    else:
        print(f"Your grade is {grade}.")
    finally:
        check_continue = input("Do you want to continue see your result again?(Yes or No): ")
        if check_continue.lower() == "no":
            result = False

print("Thank you for using the Grade Calculator. Goodbye!")