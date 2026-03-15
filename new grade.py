subjects = ["Moral Science", "GK", "Computer", "Hindi", "Drawing"]

# Define marks for each subject
Moralscience = 45
Generalknowledge = 38
Computer = 50
Hindi = 42
Drawing = 30

marks = [Moralscience, Generalknowledge, Computer, Hindi, Drawing]

# A simple loop to do the work for all 5 subjects in 5 lines!
for i in range(len(subjects)):
    m = marks[i]
    if m > 50: grade = "Invalid"
    elif m == 50: grade = "A"
    elif m >= 40: grade = "B"
    elif m >= 20: grade = "C"
    elif m >= 10: grade = "D"
    else: grade = "Fail"
    
    print(f"{subjects[i]}: You got {grade} grade")
