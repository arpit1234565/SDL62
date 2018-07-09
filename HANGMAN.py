import random

WORD_LIST = [
    'apple',
    'mango',
    'kiwi',
    'banana',
    'pineapple',
    'orange',
]

HANGMAN = (
    """
    x-------x
    """,
    """
    x-------x
    |
    |
    |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
)

MAX = len(HANGMAN) - 1
ALPHABETH = 'abcdefghijklmnopqrstuvwxyz'

def guess_letter(letters_guessed):
    while True:
        guess = input('Guess a letter : ').lower()
        if guess not in ALPHABETH:
            print (guess, 'is like totally not in the alphabet , try again!')
        elif guess in letters_guessed:
            print ('You already guessed {}.. PAY ATTENTION!'.format(guess))
        else:
            return guess
            
            
            
def play_hangman():
    hang_size = 0
    word_to_guess = random.choice(WORD_LIST)
    word_to_guess_spaced = ' '.join(word_to_guess)
    hidden = ['_']*len(word_to_guess)
    letters_guessed = set()
    user_guessed_word_spaced = ' '.join(hidden)
    print ("HANGMAN!")
    while hang_size < MAX:
        print
        print (user_guessed_word_spaced)
        user_guess = guess_letter(letters_guessed)
        letters_guessed.add(user_guess)
        if user_guess in word_to_guess:
            print ("\nYeah yeah.. We're all impressed.. {} is in the word woohoo..".format(user_guess))
            for i, letter in enumerate(word_to_guess):
                if user_guess == letter:
                    hidden[i] = letter
            user_guessed_word_spaced = ' '.join(hidden)
            if user_guessed_word_spaced == word_to_guess_spaced:
                print
                print (word_to_guess)
                break
        else:
            print ("{}.. Really? That's the best you can do.. Not in my word..".format(user_guess))
            hang_size += 1
            print (HANGMAN[hang_size])
    return user_guessed_word_spaced == word_to_guess_spaced

if __name__ == '__main__':
    is_winner = play_hangman()
    if is_winner:
        print ('\nYou win! Finally you did something right!')
    else:
        print ('\nGAME OVER')


