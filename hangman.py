import random
from words import words
import string

def getValidWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = getValidWord(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 0
    while len(word_letters) > 0 and lives < 5:
        # letters used
        # " ".join(['a','b','cd']) --->'a b cd' each letter used is turned into a string
        print("You have used these letters: ", " ".join(used_letters))    
        print(f'You have used {lives} out of 5')
        #tell the user what the current word is with - where the current letter need to be guessed
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: '," ".join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            lives += 1
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already used that character")
        else:
            print("Invalid character")

    print(f'Game Over! You used {lives} out of {lives} lives!')
    print(word)


# user_input = input('Type something: \n')
# print(user_input)
hangman()