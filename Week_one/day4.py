#RONDAM LOVE SCORE
import random
random_integer = random.randint(1, 10)
print(random_integer)
random_float = random.random()*10
print(random_float)
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

#HEAD OR TAIL
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
random_side = random.randint(0,1)
if random_side == 1:
    print("Head")
else:
    print("Tails")

#LIST
states_of_america = ["Deleware", "Dennis", "New york", "oyo", "ibadan", "osun", "ilabe", "ikeja", "ilesha", "lagos", "ajala", "challenge", "toll gate"]
print(states_of_america[:2])
states_of_america[0]= "tech u"
print(states_of_america[0])
states_of_america.append("lagoon")
print(states_of_america)
states_of_america.extend(["galaga", "ijesha"])
print(states_of_america)

#RANDOM BILL PAYMENT
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
namesAsCSV = input("Give me everybody's name, separated by coma. Angela, Ben, James ")
names = namesAsCSV.split(", ")
num_items= len(names)
random_choice= random.randint(0, num_items -1)
person_who_will_pay = names[random_choice]
person_who_will_pay =random_choice(names)
print(person_who_will_pay + "is going to buy meal today?")

#LIST
states_of_america = ["idaho","arizona","new mexico","Deleware", "Dennis", "New york", "oyo", "ibadan", "osun", "ilabe", "ikeja", "ilesha", "lagos", "ajala", "challenge", "toll gate"]
print(states_of_america[-15])
fruits = ["Strawberry", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "pears"]
vegetables = ["Spinach", "kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

#TREASURE GAME
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1,row2, row3]
print(f"{row1}\n {row2}\n {row3}")
position = input("Where do you want to put the treasure? ")
horizonal = int(position[0])
vertical = int(position[1])
selected_row =(map[vertical -1])
selected_row[horizonal -1] = "X"
print(f"{row1}\n {row2}\n {row3}")

#ROCK,PAPER.SCISSORS
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor.\n " ))
computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")
if user_choice == 0 and computer_choice ==2:
    print("You wins")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice> user_choice:
    print("You lose")
elif user_choice> computer_choice:
    print("You wins")
elif computer_choice == user_choice:
    print("It is a draw")
elif user_choice >= 3 or user_choice < 0:
    print("You typed invalid number, ")
#OR
#ROCK,PAPER.SCISSORS
import random
user_choice = int(input("Enter what you choose. 0 for Rock, 1 for Paper, 2 for scissors\n"))
computer_choice = random.randint(0,2)
print(f"Computer choice is {computer_choice}")
if user_choice == 0 and computer_choice == 2:
    print("You wins")
elif user_choice == 2 and computer_choice == 1:
    print("You wins")
elif user_choice == 1 and computer_choice == 0:
    print("You wins")
elif user_choice >= 3 or user_choice < 0:
    print("Your choice is invalid")
elif user_choice == computer_choice:
    print("It is a draw")
else:
    print("Computer wins")

