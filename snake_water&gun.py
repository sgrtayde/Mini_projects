import random


def game_win(user, computer):
    if user == computer:
        return None
    

    # snake vs water
    if user == "s" and computer == "w":
        return True
    if user == "w" and computer == "s":
        return False

    # water vs gun 
    if user == "w" and computer == "g" :
        return True
    if user == "g" and computer == "w":
        return False
    
    # gune vs snake
    if user == "g" and computer == "s":
        return True
    if user == "s" and computer == "g":
        return False



rand_no = random.randint(1,3)

print("Computer's turn: snake (s), water (w), gun (g) ")

if rand_no == 1:
    computer = "s"
elif rand_no == 2:
    computer = "w"
else:
    computer = "g"


user = input("Your turn : snake(s), water(w), gun(g) ").lower()

resule = game_win(user,computer) # return true if you Win!,Fales for lose Non for drow

print(f"\nYou chose: {user}")
print(f"\nComputer chose: {computer}")


if resule is None:
    print("its a drow!")
elif(resule):
    print("You win!")
else:
    print("You lose!")





