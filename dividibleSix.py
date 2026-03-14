# Question: Check if a number is divisible by 2, 3, and 6. Explanation: If a number is divisible by both 2 and 3, it is also divisible by 6.
# Input: Number = 18
# Output: Satisfy

def divisibleBySix(num):
    if num%2==0 and num%3==0:
        return "Satisfy"
    else:
        return "Do not satisfy"
    
print(divisibleBySix(18))