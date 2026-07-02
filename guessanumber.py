import random
num=[1,2,3,4,5,6,7,8,9,10]
guess=int(input("Guess a number between 1 to 10: "))
comp=random.choice(num)
if guess==comp:
    print("you are the Winner! Computer chose: ",comp)
elif guess > 10 or guess < 1:
    print("Please enter a number between 1 to 10")
else:
    print("Computer is the Winner! compurter chose: ",comp)
