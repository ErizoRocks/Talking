import random
from datetime import datetime
CurDate = datetime.today().day
name = input("what is your name?")


print("Nice to meet you", name,"!")

questionN = random.randint(1, 5)
if questionN == 1:
  Fcolor = input ("What is your favorite color?")
  print ("I love", Fcolor, "! My favorite color is seafoam green.")

if questionN == 2:
  NPet = input("How many pets do you have")
  print ("I have a bug named Syntax.")  

if questionN == 3:
  Bday = input("When is your birthday?")
  if Bday == CurDate:
    print("OH!")
    print("Happy birthday to you,")
    print("Happy birthday to you,")
    print("Happy birthday to", name,",")
    print("Happy birthday to you!")
  else:
    print("Cool! Mine is February 30th!")

if questionN == 4:
    FavB = input("What is your favorite book?")
    print ("Awesome! I love", FavB)

if questionN == 5:
  CHhoice = random.randint(1,3)
  FavF = input("What is your favorite food?")
  if CHhoice == 1:
    print("I haven't tried", FavF, "before. My favorite food is chocolate cake.") 
  else:
    print("I love", FavF,", but my favorite food is Chocolate cake.")

print("It was great to meet you", name, ". See you soon!")
print("Bye!")