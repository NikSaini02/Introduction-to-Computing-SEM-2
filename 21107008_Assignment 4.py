# Assignment 4 
# Name : Nikhil Saini 
# SID : 21107008
# Branch : Mechanical Engg

# Question no. 1

marks = int(input("Enter the marks obtained : "))

if marks < 25:
    print("The grade obtained is F")
elif(marks>=25 and marks<45):
    print("The grade obtained is E")
elif(marks>=45 and marks<50):
    print("The grade obtained is D")
elif(marks>=50 and marks<60):
    print("The grade obtained is C")
elif(marks>=60 and marks<80):
    print("The grade obtained is B") 
elif(marks>=80 and marks<=100):
    print("The grade obtained is A")
else: 
    print("Provide the input from O to 100 only") 
     
# Question no. 2

year=int(input("Enter a year : "))

if year%400==0:
    print("yes , leap year")
elif year%4==0 and year%100!=0:
    print("yes, leap year")
else:
    print("not a leap year") 

# Question no. 3

from random import randint


for i in range(1,11):
    num1=randint(1,10)
    num2=randint(1,10)
    print(f" ques {i}-->  {num1}X{num2}")
    a=int(input("Enter answer of ques 1: "))
    if a == num1*num2 :
        print("Right !")
    else:
        print(f"Wrong , answer is {num1*num2}") 

# Question no. 4

x=200

for i in range(x):

    if i % 5 == 2:
       if i % 6 == 3:
          if i % 7 == 2:
             print(i, 'candies are in the bowl!') 
             
