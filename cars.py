# Question: Calculate how many cars are needed for a given number of people. Explanation: Divide total people by 5 and round up using ceiling logic. 
# Input: Members = 17 
# Output: Cars needed = 4

def carsNeeded(members):
    if members%5==0:
        cars=members//5
    else:
        cars=(members//5)+1
    
    return cars

print("Cars needed: ",carsNeeded(17))
