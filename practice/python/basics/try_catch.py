try:
    number = int(input("Enter a number to divide 1:"))
    print(1/number)
except ZeroDivisionError:
    print("You cannot divide number with zero")
except ValueError:
    print("You cannot divide a number with strings.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("The operation is successful.")