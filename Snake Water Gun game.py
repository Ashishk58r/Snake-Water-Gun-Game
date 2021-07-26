import random
lst = ["Rock", "Paper", "Scissors"]
compcount = 0
usercount = 0
tie = 0
for e in range(10):
    comp = random.choice(lst)
    user = input("Enter your Choice between \n \t Rock \t Paper \t Scissors").capitalize()
    if comp == "Rock" and user == "Paper":
        print("User wins")
        usercount+=1
    if comp == "Rock" and user == "Scissor":
        print("Computer Win")
        compcount+=1
    if comp == "Paper" and user == "Rock":
        print("Computer wins")
        compcount+=1
    if comp == "Paper" and user == "Scissors":
        print("You Win")
        usercount+=1
    if comp == "Scissors" and user == "Paper":
        print("Computer wins")
        compcount+=1
    if comp == "Scissors" and user == "Rock":
        print("You Win")
        usercount+=1
    if comp == user:
        tie+=1
        print("It was a tie")

print(f"Computer won {compcount} number of times")
print(f"User won {usercount} number of times")
print(f"Game tied for {tie} number of times.")
if (compcount>usercount):
    print("Computer wins the game")
if (compcount<usercount):
    print("User wins the game")
if (compcount == usercount):
    print("There was a tie between User and Computer")
