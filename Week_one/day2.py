# print(len(input("Enter your name: ")))
# print("hello " [0] )
#
# #Data_type
#
# #String
#
# "Hello"[4]
# print("123" + "345")
#
# #integer
# print(123 + 345)
#
# #Float
# 3.12344
#
# #Boolean
# True
# False

# num_char = len(input("What is your name: "))
# new_num_char= str(num_char)
# print("Your name as " , new_num_char , "characters.")
# print(type(num_char))

# a = float(123)
# print(type(a))
# print(70 + float(100.2))

# two_digit_number= input("Type a two digit number: ")
# print(type(two_digit_number))
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
# result = int(first_digit) + int(second_digit)
# print(result)

# a=3 + 5
# b=7 - 3
# c = x * 2
# d=6/3
# 2**3
# print(type (6/3))
# PEMDAS
# ()
# **
# *
# /
# +
# -
# print(3* 3+3/3-7)

# height= float(input("Enter your height in meter: "))
# weight= float(input("Enter your weight in kg: "))
# bmi = int(weight)/float(height)**2
# bmi_as_int = int(bmi)
# print("Your bmi is",bmi_as_int)

# print(round(8/3))
# result = 4/2
# result /= 2
# print(result)
#
# score = 5
# score -= 1
# print(score)

# score =0
# height = 1.8
# isWining = True
# print(f"your score is {score} ,your height is {height}, your isWining is {isWining}")

# age = input("What is your current age?. ")
# age_as_int = int(age)
# years_remaining = 90 - age_as_int
# days_remaining = years_remaining*365
# week_remaining = years_remaining*52
# months_remaining = years_remaining*12
# message = f"You have {days_remaining} days, {week_remaining} weeks, {months_remaining} months and {years_remaining} years left"
# print(message)

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $ "))
# tip = int(input("How much tip would you like to give? 10, 12, or 15. "))
# people = int(input("How many people to slit the bill? "))
# # bill_with_tip = bill * (1 + tip/100)
# # print(bill_with_tip)
# # or
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip+tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_percent = total_bill / people
# final_amount = round(bill_per_percent, 2)
# print(f"Each person should pay ${final_amount}")