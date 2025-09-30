import random

print("------ Rock-Paper-Scissors Game ------")

# Initialize scores
user_score = 0
computer_score = 0

# Choices
choices = ["rock", "paper", "scissors"]

while True:
    # User Input
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    # Computer Selection
    computer_choice = random.choice(choices)

    # Display choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game Logic
    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You Win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1

    # Display scores
    print(f"Score --> You: {user_score} | Computer: {computer_score}")

    # Play Again Option
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break
