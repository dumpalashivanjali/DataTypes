# Question: Calculate the average of marks in 3 subjects.
# Input: - Maths = 85 - Physics = 90 - Chemistry = 88
# Output: - Average marks: 87.67

def AverageMarks(M,P,C):
    average = (M+P+C)/3
    return average

print("Average marks: ",round(AverageMarks(85,90,88),2))