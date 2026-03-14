# Question: Find the second largest number among three inputs. Explanation: Use sorting or nested conditions to find the second largest value.
# Input: A = 10, B = 25, C = 18 
# Output: Second biggest: 18

def secondBiggest(num1, num2, num3):
    arr=[num1, num2, num3]
    arr.sort()
    return arr[1]

print("SecondBiggest: ",secondBiggest(10,25,18))