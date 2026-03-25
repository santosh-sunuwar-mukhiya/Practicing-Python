# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
# Equation of an area of a triangle is,
# area = (1/2)*base*height
# 2.Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle".
# Based on shape type it will calculate area. Equation of rectangle's area is
#rectangle area=length*width

def calculate_area(base, height, shape="triangle"):
    if shape.lower() == "triangle":
        area = (base * height) / 2
    elif shape.lower() == "rectangle":
        area = base * height
    else:
        print("Error: Input Triangle or Rectangle as Shape.")
        area=None
    return area

base = float(input("Enter the base: "))
height = float(input("Enter the height: "))
shape = input("Enter the shape of the object(Triangle or Rectangle):")
area = calculate_area(base, height, shape)

print(f"Area of {shape}: {area}")