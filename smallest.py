# Question: Find the smallest number among two. Explanation: Use comparison operators (<) to find the smaller value.
# Input: A = 4, B = 7 
# Output: Smallest is: 4

def smallest(num1,num2):
    if num1<num2:
        return num1
    else:
        return num2
    
print("Smallest is: ",smallest(4,7))