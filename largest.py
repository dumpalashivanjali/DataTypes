# Question: Find the biggest number among two. Explanation: Use comparison operators (>) to check which number is greater.
# Input: A = 4, B = 7 
# Output: Biggest is: 7

def largest(num1, num2):
    if num1>num2:
        return num1
    else:
        return num2
    
print("Biggest is:",largest(4,7))