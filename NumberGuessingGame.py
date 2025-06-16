import random

def start_game():
    # Display welcome message and rules
    print("""
    ===========================================
    Welcome to the Number Guessing Game!
    ===========================================
    Rules:
    1. The computer will select a random number between 1 and 100.
    2. Choose a difficulty level by entering:
        1 - Easy (10 attempts)
        2 - Medium (7 attempts)
        3 - Hard (5 attempts)
    3. After each guess, I'll tell you if the number is higher or lower.
    4. Guess correctly before your attempts run out!
    ===========================================
    """)
    
    # Computer selects random number
    secret_number = random.randint(1, 100)
    
    # Difficulty selection with number input
    attempts = 0
    while attempts == 0:
        level = input("Choose difficulty (1-Easy, 2-Medium, 3-Hard): ")
        if level == '1':
            attempts = 10
        elif level == '2':
            attempts = 7
        elif level == '3':
            attempts = 5
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
    
    # Game loop
    guessed = False
    for attempt in range(1, attempts + 1):
        print(f"\nAttempt {attempt} of {attempts} - ", end="")
        
        # Validate user input
        while True:
            try:
                guess = int(input("Guess the number (1-100): "))
                if 1 <= guess <= 100:
                    break
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        
        # Check guess
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed it in {attempt} attempts!")
            guessed = True
            break
        elif guess < secret_number:
            print("The number is HIGHER than your guess.")
        else:
            print("The number is LOWER than your guess.")
    
    # End game message if user didn't guess
    if not guessed:
        print(f"\nGame over! You've run out of attempts. The number was {secret_number}.")

# Start the game
if __name__ == "__main__":
    start_game()