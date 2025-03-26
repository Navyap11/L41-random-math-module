import random 
while True:
    user_options= print("Please enter rock, paper or scissors")
    possible_choices= ["rock", "paper", "scissors"]
    user= input("Choose one of the three: ")
    computer= random.choice(possible_choices)
    
    print("You chose: ",user," and the computer chose: ",computer)

    if user==computer:
        print("It's a tie! You both chose ",user)
    elif user=="rock" and computer=="scissors":
        print("User wins! Rock kills scissors!")
    elif user=="scissors" and computer=="rock":
        print("Computer wins! Rock kills scissors!")
    elif user=="Scissors"and computer=="paper":
        print("User wins! Scissors cut through paper!")
    elif user=="paper" and computer=="scissors":
        print("Computer wins! scissors cut through paper!")
    elif user=="paper" and computer=="rock":
        print("User wins! Papaer covers rock!")
    elif user=="rock"and computer=="paper":
        print("Computer wins! paper covers rock!")
    else:
        print("Error")
