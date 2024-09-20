import random

# Function to get the computer's choice
def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Function to play a single round
def play_round():
    # Prompt user for input
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Get computer's choice
    computer_choice = get_computer_choice()

    # Display choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine and display result
    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result

# Main function to play the game with score tracking and multiple rounds
def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        print("\n--- Round", rounds + 1, "---")
        result = play_round()

        # Update scores based on the result
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        rounds += 1

        # Display current scores
        print(f"\nCurrent Score:\nYou: {user_score} | Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    # Display final scores
    print(f"\nFinal Score after {rounds} round(s):\nYou: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")

# Start the game
play_game()
