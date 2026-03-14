age = 18
print("Age after 5 years: ",age+5)
height = 1.7
print("Height in cm: ",height*100)
print("Is age older than 18:",age>=18)
print("Is height > 1.5m:",height>1.5)
is_enrolled=True
print("Is adult and enrolled:",age>=18 and is_enrolled)
print("Is younger than 18 or taller than 1.6m :",age<18 or height>1.6)

subjects = ["Math","Physics","Biology"]
print("Is Math in subjects:","Math" in subjects)
print("Is History not in subjects:","History" not in subjects)


subjects_copy = subjects
subjects_clone = subjects.copy()

print(subjects_copy is subjects)
print(subjects_clone is subjects)
print(subjects_clone==subjects)


