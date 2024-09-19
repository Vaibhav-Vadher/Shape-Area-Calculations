# Python program to compute Surface Area of Cuboid
print("Surface Area of Cuboid")

# input / assignment
length = int(input("Entre the lenght : "))
breadth = int(input("Entre the breadth : "))
height = int(input("Enter the Height : "))

# compute / process
area = 2 * (length*breadth + breadth*height + height*length)

# output / results
print(f"Length  = {length}, m")
print(f"Breadth = {breadth} m")
print(f"Height = {height} m")
print(f"\nSurface Area of Cuboid = {area} sq.m")
