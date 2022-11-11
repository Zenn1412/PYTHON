print("Welcome to Grade Conversion")
# input user Name and Grade:
#while to loop
while True:
    studentName = str(input("What is your Name: "))
    studentNumber =str(input("What is your Student number: "))
    subject =str(input("Input your Subject: "))
    grade = float(input("What is your Grade: "))
#conditional statement which is going to change the students' grade
    if 96 <= grade <= 100:
        print(str(studentNumber) + "-" + str(studentName) + "'s grade in " + str(subject) +  " is equivalent to: " + "4.0")
    elif 90 <= grade <= 95:
        print(str(studentNumber) + "-" + str(studentName) + "'s grade in " + str(subject) +  " is equivalent to: " + "3.5")
    elif 84 <= grade <= 89:
        print(str(studentNumber) + "-" + str(studentName) + "'s grade in " + str(subject) +  " is equivalent to: " + "3.0")
    elif 78 <= grade <= 83:
        print(str(studentNumber) + "-" + str(studentName) + "'s grade in " + str(subject) +  " is equivalent to: " + "2.5")
    elif 72 <= grade <= 77:
        print(str(studentNumber) + "-" + str(studentName) + "'s grade in " + str(subject) +  " is equivalent to: " + "2.0")
    elif 66 <= grade <= 71:
        print(str(studentNumber) + "-" + tr(studentName) + "'s grade in " + str(subject) +  " is equivalent to: " + "1.5")
    elif 60 <= grade <= 65:
        print(str(studentNumber) + "-" + str(studentName) + "'s grade in " + str(subject) +  " is equivalent to: " + "1.0")
    elif grade <= 59:
        print(str(studentNumber) + "-" + str(studentName) + "'s grade in " + str(subject) +  " is equivalent to: " + "R")
    else:
        print("please enter a number that is included on the scale!")

#ask if the user wants to Input grade again. if the answer is No, Break the loop
    repeat_process = input("Do you want to input your grade again? (Y if yes / N if No: ")
    if repeat_process == "N":
        break
    else:
          continue
