# Question: Determine whether a number is even or odd. Explanation: A number is even if it is divisible by 2. Otherwise, it’s odd.
# Input: Number = 6 
# Output: Even number

def EvenOdd(num):
    if num%2==0:
        return "Even number"
    else:
        return "Odd number"

print(EvenOdd(6))