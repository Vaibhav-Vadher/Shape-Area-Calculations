# Python program to compute Area of Trapezoid
print("Area of Trapezoid")

# input / assignment
length_1 = int(input("Enter the frist Length : "))
length_2 = int(input("Enter the second Length : "))
height = int(input("Enter the Height : "))

# compute / process
area = 1/2 * (length_1 + length_2) * height

# output / results
print(f"Length of Side A = {length_1} m")
print(f"Length of Side B = {length_2} m")
print(f"Height = {height} m")
print(f"\nArea of Trapezoid = {area} sq.m")
