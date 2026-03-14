# Question: Break the total amount into denominations.
# Input: - Amount = 3700
# Output: - 1000s: 3 - 500s: 1 - Remaining: 200

def amountChange(amount):
    thousands = amount // 1000
    amount=amount%1000
    fivehund =amount //500
    amount =amount%500
    remaining=amount
    return (thousands,fivehund,remaining)

a,b,c=amountChange(3700)
print(f"1000s:{a} - 500s:{b} - Remaining:{c}")