import random

from words import words
import string
def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word: # when it stops iterating we get a word that has no a space or dash init
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has guessed

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters already used
        #' '.join(['a', 'b', 'cd']) --> 'a b cd' turns list into strings separated by spaces
        print("You have", lives, " lives left and used these letters: ", ' '.join(used_letters))

        #what current word is (ie W-RD)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1 # takes away a life if wrong
                print("Letter is not in word")
        
        elif user_letter in used_letters:
            print("You already used that character. Please try again.")
    #gets here when len(word_letters) == 0 OR when lives == 0

    if lives == 0:
        print("You died, sorry The word was", word)
    else:
        print("You guessed the word", word, '!!')
# user_input = input("Type Something: ")
# print(use_input)
hangman()