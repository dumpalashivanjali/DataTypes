# Question: Check if a number is a perfect square. Explanation: A number is a perfect square if the square of its square root equals the number. 
# Input: Number = 49 
# Output: Perfect square

def perfectSquare(num):
    root = num**0.5
    if num==root**2:
        return "Perfect square"
    else:
        return "Not Perfect square"
    
print(perfectSquare(49))