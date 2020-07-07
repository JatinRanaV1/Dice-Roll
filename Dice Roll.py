import random
min = 1
max = 6

roll_again = "yes"
while roll_again == "yes" or roll_again == "y" or roll_again == "Y" or roll_again == "Yes" or roll_again == "YES":
    x=int(input("How many dices to roll: "))
    if x<=0:
       print("Wrong input...Enter atleast one.")
    elif x==1:
       print("Rolling the dice...")
       print("The value is....")
       print(random.randint(min, max))
    else:
       print("Rolling the dices...")
       print("The values are....")
       for i in range (0,x):
           print(random.randint(min, max))
    roll_again = input("Roll the dices again?... : ")