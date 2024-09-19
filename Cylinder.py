import math
# Python program to compute Surface Area of Cylinder
print("Surface Area of Cylinder")

# input / assignment
radius = int(input("Enter the radius : "))
height = int(input("Enter the height : "))

# compute / process
area = (2 * math.pi * radius * height) + (2 * math.pi * radius ** 2)

# output / results

print(f"Radius = {radius} m")
print(f"heigth = {height} m")
print(f"\nSurface Area of Cylinder = {area} sq.m")