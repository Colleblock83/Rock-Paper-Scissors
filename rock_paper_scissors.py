import random
hedr = "Second try of Rock Paper Scissors"
middle = hedr.center(130)
round = 0
print(middle)

print("Please choose an option below: ")
for alf in["Rock", "Paper", "Scissors", "Enter 6 to end the program."]:
    print(alf)
print("")
while True:
    choices = ["Rock", "Paper", "Scissors"]
    pc_choice = random.choice(choices)
    round += 1
    print(f"Round {round}")
    eingb = input("Option: ")
    if eingb == "Rock":
        if eingb == pc_choice:
            print("Correct! You won.")
        else:
            print("Nope! Nice try haha!")
    elif eingb == "Paper":
        if eingb == pc_choice:
            print("Correct! You won.")
        else:
            print("Nope! Nice try haha!")
    elif eingb == "Scissors":
        if eingb == pc_choice:
            print("Correct! You won.")
        else:
            print("Nope! Nice try haha!")
    elif eingb == "6":
        input("God bless you, press any key to end the program...")
        break




