# Find the area of a triangle given all 3 sides.
import numpy as np

# Side Variables

a = np.float64(input("a:"))
b = np.float64(input("b:"))
c = np.float64(input("c:"))

# Step 1: Determine the Semiperimeter
# Half of the sum of the sidelengths
semiperimeter = s = (a + b + c) / 2

# Step 2: Determine the area.
# Sqrt of the semiperimeter distributed over the sides.
area = np.sqrt((s * (s-a) * (s-b) * (s-c)))

print("The area of the triangle is:", area)
