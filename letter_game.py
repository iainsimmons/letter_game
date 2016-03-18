import os
import random
import sys
from time import sleep


words = []


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def quit():
    clear()
    print('OK, bye!')
    sys.exit()


def play_again():
    if input('Want to play again? [Y/n]\n\n> ').lower() == 'n':
        quit()
    else:
        play()


def guessed_correct(word, whole=False):
    clear()

    if whole:
        print(
            "\nAwesome! You guessed the word '{}' correctly!\n".format(
                word))
    else:
        print(
            "\nShiny! You guessed all the letters in the word '{}'!\n".format(
                word))

    play_again()


def show_status(word, guesses):
    clear()
    display = ['_' for _ in word]
    incorrect = []

    for guess in guesses:
        if guess not in word:
            incorrect.append(guess)
        else:
            for index, letter in enumerate(word):
                if letter == guess:
                    display[index] = guess

    print('\nWord [{}]: {}\nIncorrect: {}\n'.format(
            len(word), ' '.join(display), ', '.join(incorrect)))

    if '_' not in display:
        guessed_correct(word)


def get_guess(word):
    guess = input("Guess a letter, or the whole word:\n" +
        "(or type 'quit' to exit)\n\n> ")

    if not guess.isalpha():
        print("Please use only letters from 'a' through 'z'\n")
        return get_guess(word)

    if guess.lower() == 'quit':
        quit()

    if guess.lower() == word:
        guessed_correct(word, whole=True)

    return guess.lower()


def play():
    word = random.choice(words)
    max_guesses = 7 if len(word) < 7 else 10
    guess_count = 0
    guesses = []
    show_status(word, guesses)

    while guess_count < max_guesses:
        print('Guesses left: {}\n'.format(max_guesses - guess_count))
        guesses.append(get_guess(word))
        show_status(word, guesses)
        guess_count += 1

    print("Sorry, you ran out of guesses for the word '{}'\n".format(word))
    sleep(2)
    play_again()


while True:
    clear()

    if __name__ == '__main__':
        file_path = sys.argv[1]
    else:
        file_path = input(
            "Please provide the path to a text file " +
            "with a list of single words separated by new lines:" +
            "\n(or type 'quit' to exit)\n> ")

    try:
        if file_path.lower() == 'quit':
            quit()

        with open(file_path, newline='') as word_file:
            words = [word.strip() for word in word_file
                     if word.strip().isalpha()]

        if len(words) < 1:
            raise ValueError

        break

    except EOFError:
        sys.exit(1)
    except (IndexError, FileNotFoundError, ValueError):
        pass

play()
