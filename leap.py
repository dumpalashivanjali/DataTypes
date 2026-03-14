# Question: Check if a given year is a leap year. Explanation: A year is a leap year if it is divisible by 4, and (not divisible by 100 unless divisible by 400). 
# Input: Year = 2024 
# Output: Leap year

def leapYear(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return "Leap year"
    else:
        return "Not Leap year"
    
print(leapYear(2024))