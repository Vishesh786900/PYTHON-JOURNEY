import random
list=["Stone","Paper","Scissors"]
input=input("Enter your choice (stone/paper/scissors): ")
comp_choice=random.choice(list)
if input==comp_choice:
    print("It's a tie!")
elif(input=="Stone" and comp_choice=="Scissors")or(input=="Paper" and comp_choice=="Stone")or(input=="Scissors"and comp_choice=="paper"):
    print("You are the winner! Computer chose: ",comp_choice)
else:
    print("computer is the winner! Computer chose: ",comp_choice)

