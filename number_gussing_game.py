import random

print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 100.")
print("Your goal is to guess it in the fewest attempts!\n")

high_score = None 

while True:
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (or type 'quit' to exit): ")

        if guess.lower() == 'quit':
            print("Thanks for playing! Goodbye.")
            exit()

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f" Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            
            if high_score is None or attempts < high_score:
                high_score = attempts
                print(f" New High Score: {high_score} attempts!")
            else:
                print(f" High Score so far: {high_score} attempts.")
            break 

   
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Final High Score:", high_score)
        break
    print("\nStarting a new round...\n")

