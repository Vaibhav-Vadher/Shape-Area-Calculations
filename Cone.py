import math
# Python program to compute Surface Area of Cone
print("Surface Area of Cone")

# input / assignment
radius = int(input("Enter Radius : "))
slant_height = int(input("Enter Slant Height : "))
height = int(input("Enter Height : "))



# compute / process
area1 = math.pi * radius * (radius + slant_height)
area2 = math.pi * radius * (radius + math.sqrt(height**2 + radius**2))

# output / results

print(f"Radius = {radius} m")
print(f"heigth = {height}m")
print(f"Slant height = {slant_height} m")
print(f"\nSurface Area of Cone(with slant hright) = {area1:.2f} sq.m")
print(f"\nSurface Area of Cone(without slant hright) = {area2:.2f} sq.m")