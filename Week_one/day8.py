def greet():
    print("Hello peeps")
    print("How are you lads?")
    print("How is everything? ")
greet()

# Function that allows for input
def greet_with_name(name):
    print("Hello ", name)
    print("How are you lads?", name)
    print("How is everything? ", name)
greet_with_name("Angela")

#Function with more than 1 input
def greet_with(name, location):
    print("Hello:  ", name)
    print("What is it like in location: ",location)
greet_with("Wale", "Nowhere")
#Function with keyword arguments
greet_with(name="Wale", location="Oyo")

#METRICS
import math
def point_calc(height, width, cover):
    area = height * width
    num_of_can = math.ceil(area/cover)
    print(f"You will need {num_of_can} cans of point.  ")
test_h = int(input("What is the height of wall?. "))
test_w = int(input("Width if wall?. "))
coverage = 5
point_calc(height = test_h, width = test_w,cover=coverage)

# #Prime number
def prime_checker(number):
    is_prime = True
    for i in range(2,number -1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It,s a prime number")
    else:
        print("It's a not a prime number. ")
