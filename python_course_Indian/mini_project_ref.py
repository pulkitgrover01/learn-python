

# import random

# def get_computer_choice():
#     choices = ['rock', 'paper', 'scissors']
#     return random.choice(choices)

# def get_user_choice():
#     user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
#     while user_input not in ['rock', 'paper', 'scissors']:
#         print("Invalid choice. Please try again.")
#         user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
#     return user_input

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == 'rock' and computer_choice == 'scissors') or \
#          (user_choice == 'paper' and computer_choice == 'rock') or \
#          (user_choice == 'scissors' and computer_choice == 'paper'):
#         return "You win!"
#     else:
#         return "You lose!"

# def play_game():
#     user_choice = get_user_choice()
#     comp_choice = get_computer_choice()
#     print(f"Computer chose: {comp_choice}")
#     result = determine_winner(user_choice, comp_choice)
#     print(result)

# # Play the game
# play_game()


