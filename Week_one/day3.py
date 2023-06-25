#FIRST ROLLER COASTER
print("Welcome to rollerCoaster! ")
height = int(input("What is your height in cm? "))
if height >= 120:
    print(f"You can ride rollerCoaster! , Your height is", height)
else:
    print("Sorry, you have to grow taller before you can ride")

number = int(input("Which number do you want to divides? "))
if number % 2 == 0:
    print("This is even number. ")
else:
    print("This is odd number.")

#SECOND ROLLERCOASTER.
print("Welcome to rollerCoaster! ")
height = int(input("What is your height in cm? "))
if height >= 120:
    print(f"You can ride rollerCoaster! , Your height is", height)
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5. ")
    elif age <= 18:
        print("Please pay $40. ")
    else:
        print("Please pay $12. ")
else:
    print("Sorry, you have to grow taller before you can ride")

#BMI
height = float(input("Enter your height in meter: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight/height **2)
print(bmi)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are underweight. ")
elif bmi < 25:
    print(f"Your bmi is  {bmi}, you have normal weight. ")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight. ")
elif bmi < 35:
    print(f"Your bmi is  {bmi}, you are obese. ")
else:
    print(f"Your bmi is {bmi},you are clinically obese. ")

year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year.")
        else:
            print("Not a leap year.")
    else:
        print("A leap year.")
else:
    print("it is not a leap year")

#THIRD rollerCoaster
print("Welcome to rollerCoaster! ")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print(f"You can ride rollerCoaster! , Your height is", height)
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket is $5. ")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $40. ")
    else:
        bill = 12
        print("Adult ticket is $12. ")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += bill + 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")

#Pizza deliveries
print("Welcome to python pizza deliveries! ")
size = input("What is the size of pizza you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill +=15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}")

#welcome to rollerCoaster
print("Welcome to rollerCoaster! ")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print(f"You can ride rollerCoaster! , Your height is", height)
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket is $5. ")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7. ")
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay. have a ride on us. ")
    else:
        bill = 12
        print("Adult ticket is $12. ")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += bill + 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")

#LOVE CALCULATOR
print("Welcome to the Love calculator! ")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t+r+u+e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l+o+v+e
#AND
love_score = int(true) + int(love)
print(love_score)
if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together")
elif (love_score >= 40) or (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together ")


choice1= input('You are at a crossroad, where do you want to go? Type "left" or "right". ').lower()

if choice1 == "left":
    choice2= input("you have to come to lake There is an island in the middle of lake. Type 'wait' to wait for a boat. ").lower()
    if choice2 == "wait":
        choice3 = input("you  arrive at the island unharmed. There is a house with 3 doors. one is red, one is yellow and one is blue.").lower()
        if choice3 == "red":
            print("it is room full of fire. Game over")
        elif choice3 == "yellow":
            print("You found the treasure. You won.")
        elif choice3 == "blue":
            print("You enter a room of beast. Game over")
        else:
            print("You choose the door that does not exist. Game over. ")
    else:
      print("You got attacked by angry trout. Game over")
else:
    print("You fell in to hole. Game over. ")
