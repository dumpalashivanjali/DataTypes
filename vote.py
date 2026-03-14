# Question: Check if a person is eligible to vote (age >= 18). Explanation: A person is eligible to vote if their age is 18 or above.
# Input: Age = 19 
# Output: Eligible to vote

def eligibility(age):
    if age>=18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"
    
print(eligibility(19))