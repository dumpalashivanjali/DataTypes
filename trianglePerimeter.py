# Question: Calculate the perimeter of a triangle. - Formula: Perimeter = side1 + side2 + side3
# Input: - Side1 = 5, Side2 = 6, Side3 = 7
# Output: - Perimeter of triangle is: 18

def trianglePerimeter(s1, s2, s3):
    perimeter = s1 + s2 + s3
    return perimeter

print("Perimeter of triangle is: ",trianglePerimeter(5, 6, 7))