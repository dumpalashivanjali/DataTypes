# Question: Check if a number is divisible by 5 but not by 10. Explanation: Use modulo (%) to check if the number % 5 == 0 and number % 10 != 0.
# Input: Number = 25 
# Output: Satisfy

def divisible(num):
    if num%5==0 and num%10!=0:
        return "Satify"
    else:
        return "Do not satisfy"
    
print(divisible(25))