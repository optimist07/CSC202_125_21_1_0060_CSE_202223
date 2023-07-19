#creating your own class
#class name in python always has its first letter capitalized

class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        #print("New user being created...")

    #creating another method
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("007", "Gafar")

#print(user_1.username, user_1.id)

user_2 = User("070", "Optimist")

#print(user_2.username, user_2.id)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

#User_is_the_class
#user_2_is_the_object
#user1_id and username are the attribute
#initialize is the process of setting(variables, counters, switches) to their strting values at the beginning of a program or subprogram
#inti is call anytime we create new object in the class


