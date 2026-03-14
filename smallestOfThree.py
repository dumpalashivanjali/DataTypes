# Question: Find the smallest number among three. Explanation: Use comparison logic to determine the minimum value.
# Input: A = 7, B = 4, C = 9
# Output: Smallest is: 4


def smallestOfThree(num1,num2,num3):
    if num1<num2 and num1<num3:
        return num1
    elif num2<num1 and num2<num3:
        return num2
    else:
        return num3

print("Smallest is: ",smallestOfThree(7,4,9))