message = input().lower()
found=0
for ch in message:
    if ch == "x":
        found+=1

if found>=1:
    print("Secret letter found!")
else:
    print("No secret letter in the message")
