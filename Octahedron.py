import math
# Python program to compute Surface Area of Octahedron
print("Surface Area of Octahedron")

# input / assignment
side = int(input("Enter the sides of Octahedron : "))

# compute / process
area = 2 * math.sqrt(3) * side**2

# output / results

print(f"Side = {side} m")
print(f"\nSurface Area of Octahedron = {area} sq.m")