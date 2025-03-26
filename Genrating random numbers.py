import random
participating=True
num=str(random.randint(0,5))
print("Pick number from 0-5. If you guess right, you win! Only need to get one right to win!")

while participating:
    choose= input("Give ur best guess!\n")
    if num==choose:
        print("Correct! You Win! The number was: ",num)
        break
    else:
        print("Wrong! Try again!")