# Given an input, SSA or SSS, applies the law of COS to solve. Order doesn't matter other than keeping association between side and angle when moving from calculator to problem space.


import math

while True:
    print("Note that input angles must be in degrees. Also, its up to you to make sure variable correspondence is accurate.\n")
    given = int(input("Please enter 1 for SSA, or 2 for SSS.\n"))
    if given == 1:  # SSA
        print("\nPlease enter the information in order of side, side, angle.")

        # Side 1 or a
        s1 = float(input("\nSide 1:\n "))

        # Side 2 or b
        s2 = float(input("\nSide 2:\n "))

        # Angle 3 or C.
        a3 = float(input("\nPlease enter the angle in degrees:\n "))

        # Find last side
        s3 = math.sqrt(s1 ** 2 + s2 ** 2 - (2 * s1 * s2 * math.cos(math.radians(a3))))

        # Find angle 2 or B
        a2 = math.degrees(math.acos((s1 ** 2 + s3 ** 2 - s2 ** 2) / (2 * s1 * s3)))

        # Find angle 1 or A
        a1 = math.degrees(math.acos((s2 ** 2 + s3 ** 2 - s1 ** 2) / (2 * s2 * s3)))

        print("Triangle Solved.\ns1 = {}, s2 = {}, s3 = {},\na1 = {}, a2 = {}, a3 = {}\n".format(s1, s2, s3, a1, a2, a3))

    elif given == 2:  # SSS
        # Side 1 or a
        s1 = float(input("\nSide 1:\n "))

        # Side 2 or b
        s2 = float(input("\nSide 2:\n "))

        # Side 3 or c
        s3 = float(input("\nSide 3:\n "))

        # Angle 1 or A
        a1 = math.degrees(math.acos((s2 ** 2 + s3 ** 2 - s1 **2) / (2 * s2 * s3)))

        # Angle 2 or B
        a2 = math.degrees(math.acos((s1 ** 2 + s3 ** 2 - s2 ** 2) / (2 * s1 * s3)))

        # Angle 3 or C
        a3 = math.degrees(math.acos((s1 ** 2 + s2 ** 2 - s3 ** 2) / (2 * s1 * s2)))

        print("Triangle Solve.\na1 = {}, a2 = {}, a3 = {}".format(a1, a2, a3))

    else:
        print("Invalid input, try again. Be sure to enter only 1 or 2.")
        break
