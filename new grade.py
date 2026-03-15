#This is a program in which a students are given grades accroding to their marks in "grade subject".
Moralscience = int(input("Enter your marks for Moralscience :- "))
Generalknowledge = int(input("Enter your marks for GeneralKnowledge :- "))
Computer = int(input("Enter your marks for Computer :- "))
Hindi = int(input("Enter your marks for Hindi:- "))
Drawing = int(input("Enter your marks for Drawing :- "))
enteredgrade = Moralscience,Generalknowledge,Computer,Hindi,Drawing
a = ( Moralscience+Generalknowledge+Computer+Hindi+Drawing)
print("Your total marks :- " + str(a))
if(Moralscience>=40):
    print("You got 'B'grade")
elif(Moralscience>=20):
    print("You got 'C'grade")    
elif(Moralscience>=40):
    print("You got 'B'grade")
elif(Moralscience==50):
    print("You got 'A'grade")
elif(Generalknowledge>10):
    print("You got 'D'grade")
elif(Generalknowledge>=20):
    print("You got 'C'grade")
elif(Generalknowledge>=40):
    print("You got 'B'grade")
elif(Generalknowledge==50):
    print("You got 'A'grade")
else:
    print("Invalid marks entered")
if(Computer>10):
    print("You got 'D'grade")
elif(Computer>=20):
    print("You got 'C'grade")
elif(Computer>40):
    print("You got 'B'grade")
elif(Computer==50):
    print("You got'A'grade")
else:
    print("Invalid marks entred")
if(Hindi>=10):
    print("You got 'D' grade")
elif(Hindi>=20): 
    print("You got 'C' grade")
elif(Hindi>40):
    print("You got 'B' grade")
elif(Hindi==50):
    print("You got 'A'grade")
else:
    print("Invalid marks entered")  
if(Drawing > 50): # Catch errors first!
    print("Invalid marks entered")
elif(Drawing == 50):
    print("You got 'A' grade ")
elif(Drawing >= 40):
    print("You got 'B' grade ")
elif(Drawing >= 20):
    print("You got 'C' grade ")
elif(Drawing >= 10):
    print("You got 'D' grade ")
else:
    print("Invalid marks entred ")
 #Finish
