# SSA Triangle Calculator for given values.
# Tested only on ambiguous case where there were two trianges.
import numpy as np

# Given Values (Angle, Side1, Side2)
B = 34 #deg
b = 7.1
c = 2.1


# Find sin B.
Sin_B = np.sin(B * np.pi / 180)

# Find sin C.
Sin_C_1 = c * Sin_B / b

# Find angle C.
C_1_rad = np.arcsin(Sin_C_1) # Note: output in in rad.

# Convert rad to deg
C_1 = np.rad2deg(C_1_rad) #deg

C_2 = 180 - C_1

A_1 = 180 - B - C_1

A_2 = 180 - B - C_2

# Find missing sides for respective T's.
a_1 = b * np.sin(A_1 * np.pi / 180) / np.sin(B * np.pi /180)#input must be in rad.

a_2 = b * np.sin(A_2 * np.pi /180) / np.sin(B * np.pi / 180)


# Print Complete Values.

# T1: Acute
print("T1 Acute: A = {}, B = {}, C = {}, \n \
         a = {}, b = {}, c = {}".format(A_1, B, C_1, a_1, b, c))

# T2: Obtuse
print("T2 Obtuse: A = {}, B = {}, C = {}, \n \
          a = {}, b = {}, c = {}".format(A_2, B, C_2, a_2, b, c))
