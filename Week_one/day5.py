# for loop
fruits = ["Apple", "Banana", "Mango", "Cashew", "Pineapple"]
for fruit in fruits:
    print(fruit)
    print(fruit, " " + "Pie")
    print(fruits)

# to calculate the average height of student
students_height = input("Input the student heights: ").split(",")
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
print(students_height)

total_height= 0
for height in students_height:
    total_height += height
print(total_height)

number_of_students = 0
for student in students_height:
    number_of_students += 1
print(number_of_students)

average_height = round(total_height/number_of_students)
print(average_height)

student_scores = input("Input a list of student score: ").split(",")
for n in range(0, len(student_scores)):
    student_scores[n]= int(student_scores[n])
print(student_scores)
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score is {highest_score}")

# range function
for number in range(1, 11, 3):
    print(number )
# for adding number from 1 - 100
total = 0
for number in range(1, 101):
    total += number
print(total)

#OR
total = 0
for number in range(2, 101, 2):
    total += number
print(total)
#OR
total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)

# #FIZZBUZZ
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 ==0:
        print("Buzz")
    else:
        print(number)

#password generator project
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l',
           'm','n','o','p','q','r','s','t','u','v','w','x',
           'y','z','A','B','C','D','E','F','G','H','I','J','K','L',
           'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','*',',','+']
print("Welcome to the PyPassword Generator! ")
nr_letters = int(input("How many letters would you like in your Password? \n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for char in range(1, nr_letters +1):
    random_char=random.choice(letters)
    password += random_char
for char in range(1, nr_symbols +1):
    password += random.choice(symbols)
for char in range(1, nr_numbers +1):
    password += random.choice(numbers)
print(password)

password_list = []
for char in range(1, nr_letters + 1):
    password_list.append( random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")