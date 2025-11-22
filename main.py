import random
LOGO = """
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

def main():
    difficulty = ""
    allowed_guesses = 0
    player_guesses = 0
    guessed_number = 0
    random_number = random.randint(1, 100)
    print(LOGO)
    print("Welcome to The Guessing Game!")
    while difficulty != "easy" or "hard":
        difficulty = input("Please choose a difficulty. Enter 'easy' or 'hard': ")
        if difficulty == "easy":
            allowed_guesses = 10
            break
        elif difficulty == "hard":
            allowed_guesses = 5
            break
        print('Sorry, that\'s not an option. Please enter \'easy\' or \'hard\'.')
    # print(f"random_number: {random_number}")
    # print(f"allowed guesses: {allowed_guesses}")
    # print("I am thinking about a number between 1 and 100.")
    if type(guessed_number) != int:
        while type(guessed_number) != int:
            if type(guessed_number) == int:
                break
            print("Please type an integer (a whole number without decimals or fractions.")
    print("Let's play!")
    while allowed_guesses > player_guesses:
            guessed_number = int(input("Please guess my number: "))
            # print(guessed_number)
            if guessed_number == random_number:
                print("You win!")
                break
            elif guessed_number < random_number:
                print("Too low.")
            elif guessed_number > random_number:
                print("Too high.")
            player_guesses += 1
            # print(f"player_guesses: {player_guesses}")
    print("End of game.")


main()


