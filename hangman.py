import random
import sys
from colors import *

def get_word():
    file = 'random_list.txt'
    f = open(file, 'r')
    l = f.read().strip().split('\n')
    f.close()
    word = random.choice(l)
   
    return word.upper()

def play(word):
    word_completion = str(word)
    for i in range(len(word_completion)):    
        if word_completion[i].isalpha():
            word_completion = word_completion.replace(word_completion[i], '_')
        elif word_completion[i] == ' ':
            word_completion = word_completion.replace(word_completion[i], ' ')
        elif word_completion[i] == '-':
            word_completion = word_completion
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 0  
    sys.stdout.write(GREEN)
    print("Let's play Hangman!")
    print("==================")
    sys.stdout.write(RESET)

    print_hangman(tries)
    sys.stdout.write(BOLD)
    print(word_completion)
    sys.stdout.write(RESET)
    print('\n')

    while not guessed and tries < 6:
        guess = input('Please guess a letter or word: ').upper()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'You already guessed the letter {guess}')
            elif guess not in word:
                print(f'{guess} is not in the word')
                tries += 1
                guessed_letters.append(guess)
            else:
                sys.stdout.write(GREEN)
                print(f'Good job {guess} is the word!')
                sys.stdout.write(RESET)
                word_as_list = list(word_completion)
                ind = [i for i, letter in enumerate(word) if letter == guess]
                for index in ind:
                    word_as_list[index] = guess  
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
                    
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f'You already guessed the word! {guess}')
            elif guess != word:
                print(f'{guess} is not the word')
                tries += 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Not a valid guess!')
        
        print(print_hangman(tries))
        
        sys.stdout.write(BOLD)
        print(word_completion)
        sys.stdout.write(RESET)
        
    if guessed == True:
        sys.stdout.write(GREEN)
        print('You win! Congrats, you guessed the word!')
        sys.stdout.write(RESET)
    else:
        sys.stdout.write(RED)
        print(f'Sorry, you ran out of tries. The word was {word}')
        sys.stdout.write(RESET)

def print_hangman(tries):
    if tries == 0:
        sys.stdout.write(RED)
        print('\n+----+')
        print('\n|')
        print('\n|')
        print('\n|')
        sys.stdout.write(RESET)
        
    elif tries == 1:
        sys.stdout.write(RED)
        print('\n+---+')
        print('\n|   o')
        print('\n|    ')
        print('\n|    ')
        sys.stdout.write(RESET)
      
    elif tries == 2:
        sys.stdout.write(RED)
        print('\n+---+')
        print('\n|   o')
        print('\n|   |')
        print('\n|    ')
        sys.stdout.write(RESET)
      
    elif tries == 3:
        sys.stdout.write(RED)
        print('\n+---+')
        print('\n|   o')
        print('\n|  /|')
        print('\n|    ')
        sys.stdout.write(RESET)
       
    elif tries == 4:
        sys.stdout.write(RED)
        print('\n+---+')
        print('\n|   o')
        print('\n|  /|\\')
        print('\n|    ')
        sys.stdout.write(RESET)
      
    elif tries == 5:
        sys.stdout.write(RED)
        print('\n+---+')
        print('\n|   o')
        print('\n|  /|\\')
        print('\n|  /  ')
        sys.stdout.write(RESET)
      
    elif tries == 6:
        sys.stdout.write(RED)
        print('\n+---+')
        print('\n|   o')
        print('\n|  /|\\')
        print('\n|  / \\')
        sys.stdout.write(RESET)


def main():
    word = get_word()
    play(word)
    while input('Play again? (Y/N): ').upper() == 'Y':
        word = get_word()
        play(word)
    sys.stdout.write(RED)
    print('bye-bye')
    sys.stdout.write(RESET)
        
main()


