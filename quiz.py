def quiz_game():
    score = 0
    print("""Question1: What is the capital of india?
                            1.Delhi
                            2.Mumbai
                            3.Kolkata
                            4.Chennai"""
              )
    answer1=1
    choice1=int(input("Please enter the correct option: "))
    if choice1==answer1:
        print("Correct Answer!")
        score+=1
    else:
        print("Incorrect answer")
    print("""Question2: What is 5+3
                            1.3
                            2.8
                            3.33
                            4.2"""
              )
    answer2=2
    choice2=int(input("Please enter the correct option:"))
    if choice2==answer2:
        print("Correct Answer!")
        score+=1
    else:
        print("Incorrect answer")
    print("""Question3: Which language is used for python programming?
                            1.Python
                            2.Java
                            3.C++
                            4.HTML"""
              )
    answer3=1
    choice3=int(input("Please enter the correct option:"))
    if choice3==answer3:
        print("Correct Answer!")
        score+=1
    else:
        print("Incorrect answer")
        
    print("Final Score :",score)
quiz_game()
