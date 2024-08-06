import random

def guessing_game():
    attempts = 0
    
    while True:
        guess = int(input("Guess the number between 1 to 5: "))
        number = random.randint(1,5)
        
        if guess ==  number:
            print(f"You guessed the number {number} in {attempts} attempth.")
            break
        elif guess > number:
            print("Your guessed number is high")
        elif guess < number:
            print("Your guessed number is low")

        attempts += 1
  
guessing_game()
      
