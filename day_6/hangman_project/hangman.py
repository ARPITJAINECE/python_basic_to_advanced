import random


# 1 setup the game by choosing the words
def select_word():
    words = ["python", "anaconda"]
    return random.choice(words).lower()


# 2 display the current state of game
def current_state(hidden_word, correct_guess):
    display = ""
    for letter in hidden_word:
        if letter in correct_guess:
            display += letter + " "
        else:
            display += "_ "
    print(f"Word : {display.strip()}")


# 3 asking user for a new alphabet
def get_user_guess(already_guessed):
    while True:
        guess = input("Guess a letter : ").lower()
        if len(guess) != 1:
            print("Please enter a single letter!!!")
        elif not guess.isalpha():
            print("Please enter alphabets only!!!")
        elif guess in already_guessed:
            print("This alphabet is already guessed!!!!")
        else:
            return guess


# 4 Check and Update if user won or lost
def won_or_loss(guess, secret_word):
    if guess in secret_word:
        print(f"Good, {guess} is in the word!")
        return True
    else:
        print(f"You have guessed wrong word!!!")
        return False


# 5 main playing game logic
def play_game():
    secret_word = select_word()
    correct_guess = []
    all_guesses = []
    lives = 0

    print("Welcome to the world of HANGMAN !!!!")

    while lives < 6:
        current_state(secret_word, correct_guess)
        print(f"Lives remaining : {6-lives}")

        # getting a guess
        guess = get_user_guess(all_guesses)
        all_guesses.append(guess)

        # processing the game
        if won_or_loss(guess, secret_word):
            correct_guess.append(guess)
        else:
            lives += 1

        # checking for win or loss
        # using set and subset for this
        if set(secret_word).issubset(correct_guess):
            print(f"Congratulations, You have WON !!, Correct word is : {secret_word}")
            break
        else:
            print(
                f"Game Over, You ran out of lives, The correct word is : {secret_word}"
            )


# starting the game
if __name__ == "__main__":
    play_game()
