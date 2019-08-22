import random

#Problem 1
greeting= "Hello "
my_name= " Jordon "
my_age= "27"
print (greeting+" "+"my name "+ "is"+ " "+my_name+ " "+"." + "I am"+ " "+my_age+" "+"years old"+".")
print(f'{greeting} my name is {my_name} and I am {my_age} years old.')

#Problem 2
secret_word=input("enter a password: ")
secret_pw= "cookie"

while(secret_word!=secret_pw):
    secret_word=input("Guess Again: ")
    if(secret_word=='q'):
        break;

#Problem 3
for i in range(0,50+1,1):
    print(f"{i} {i} {i}")

#Problem 4
# import random
num=random.randint(1,3)
value=-2
while(value!=num):
    value=int(input("Enter a number: "))
    if(value!=num):
        print("Guess again")


