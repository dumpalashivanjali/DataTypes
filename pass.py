# # # Question: Check if a student passed all subjects (maths, physics, chemistry). Explanation: Student passes only if marks in all subjects are 35 or more.
# # # Input: Maths = 40, Physics = 36, Chemistry = 30 
# # # Output: Fail

# # def studentPerformance(math,phy,chem):
# #     if math>=35 and phy>=35 and chem>=35:
# #         return "Pass"
# #     else:
# #         return "Fail"
    
# # print(studentPerformance(40,36,30))



# # Question: Check if the student passed at least one subject. Explanation: Use logical OR to check if any one subject has marks >= 35.
# # Input: Maths = 20, Physics = 38, Chemistry = 25 
# # Output: Pass

# def studentPerformance(math,phy,chem):
#     if math>=35 or phy>=35 or chem>=35:
#         return "Pass"
#     else:
#         return "Fail"
    
# print(studentPerformance(20,38,25))



# Question: Check if the student passed any two out of three subjects. Explanation: Use a counter or logical conditions to verify two subjects >= 35.
# Input: Maths = 40, Physics = 20, Chemistry = 36
# Output: Pass

def studentPerformance(math, phy, chem):
    count = 0    
    if math >= 35:
        count += 1
    if phy >= 35:
        count += 1
    if chem >= 35:
        count += 1
        
    if count >= 2:
        return "Pass"
    else:
        return "Fail"

print(studentPerformance(40,20,36))