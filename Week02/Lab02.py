import random #built-in package

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter a number between 1 to 3 for the following choices: 1-Rock, 2-Paper, 3-Scissors: ")

playerChoice = int(playerChoice) # static type

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice should be between 1 and 3!") #print function
else:
    # Develop the game logic using if/elif/else
    computerChoice = random.randint(1, 3) #both values are inclusive!

    if playerChoice == computerChoice: #nested if statement inside another if/else statement
        print("It's tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Scissors - You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beats Rock - You win!")
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissor beats Paper - You win!")
    else:
        print("You lose!")
    
      