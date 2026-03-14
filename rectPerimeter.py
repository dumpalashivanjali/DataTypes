# Question: Calculate the perimeter of a rectangle. - Formula: Perimeter = 2 × (length + breadth)
# Input: - Length = 5 - Breadth = 3
# Output: - Perimeter of rectangle is: 16

def rectPerimeter(l,b):
    perimeter = 2*(l+b)
    return perimeter

print("Perimeter of rectangle is: ",rectPerimeter(5,3))