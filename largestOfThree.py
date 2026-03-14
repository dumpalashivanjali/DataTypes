# Question: Find the biggest number among three. Explanation: Compare each pair of numbers using if-else conditions. 
# Input: A = 7, B = 4, C = 9 
# Output: Biggest is: 9

def largestOfThree(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

print("Biggest is: ",largestOfThree(7,4,9))