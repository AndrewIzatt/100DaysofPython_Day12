import random

def startup():
    logo = """
    ░██████████░██                     ░██████                                              ░██                        ░██████                                        
        ░██    ░██                    ░██   ░██                                                                       ░██   ░██                                       
        ░██    ░████████   ░███████  ░██        ░██    ░██  ░███████   ░███████   ░███████  ░██░████████   ░████████ ░██         ░██████   ░█████████████   ░███████  
        ░██    ░██    ░██ ░██    ░██ ░██  █████ ░██    ░██ ░██    ░██ ░██        ░██        ░██░██    ░██ ░██    ░██ ░██  █████       ░██  ░██   ░██   ░██ ░██    ░██ 
        ░██    ░██    ░██ ░█████████ ░██     ██ ░██    ░██ ░█████████  ░███████   ░███████  ░██░██    ░██ ░██    ░██ ░██     ██  ░███████  ░██   ░██   ░██ ░█████████ 
        ░██    ░██    ░██ ░██         ░██  ░███ ░██   ░███ ░██               ░██        ░██ ░██░██    ░██ ░██   ░███  ░██  ░███ ░██   ░██  ░██   ░██   ░██ ░██        
        ░██    ░██    ░██  ░███████    ░█████░█  ░█████░██  ░███████   ░███████   ░███████  ░██░██    ░██  ░█████░██   ░█████░█  ░█████░██ ░██   ░██   ░██  ░███████  
                                                                                                                 ░██                                                  
                                                                                                           ░███████                                                   

        """
    print(logo)
    print("Welcome to The Guessing Game!")

def assign_difficulty():
    answer = ""
    # Deal with non-valid answers
    while answer != "easy" and answer != "hard":
        answer = input("Please choose a difficulty. Enter 'easy' or 'hard': ").lower()
    if answer == "easy":
        return "easy"
    elif answer == "hard":
        return "hard"
    return None

def limit_guesses(diff):
    if diff == "hard":
        return 5
    return 10

def get_valid_guess():
    """Prompt the user until they enter an integer between 1 and 100."""
    while True:
        raw = input("Please enter an integer between 1 and 100: ")
        try:
            guess = int(raw)
        except ValueError:
            print("That’s not an integer. Try again.")
            continue  # ask again

        if guess < 1 or guess > 100:
            print("Number must be between 1 and 100. Try again.")
            continue  # ask again

        # If we reach here, guess is valid
        return guess

def assess_guess(answer, random_num):
    if answer == random_num:
        print("You win!")
        return "win"
    elif answer < random_num:
        print("Too low.")
    elif answer > random_num:
        print("Too high.")
    return 0

def main():
    # variables
    player_guesses = 0
    random_number = random.randint(1, 100)
    startup()
    # Assign Difficulty
    difficulty = assign_difficulty()
    # Assign # of guesses depending on difficulty
    allowed_guesses = limit_guesses(difficulty)
    print("Let's play!")
    while allowed_guesses > player_guesses:
            print(f"\nGuesses remaining: {allowed_guesses - player_guesses}")
            guess = get_valid_guess()  # always returns a valid int in range
            # Validate user input
            keep_going = assess_guess(guess, random_number)
            # Determine whether game continues based on answer
            if keep_going == "win":
                break
            player_guesses += 1
    print("End of game.")

main()


