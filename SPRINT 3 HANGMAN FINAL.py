#Cameron Dyer
#Orginally created basic hangman game, however too simplistic
#This is my Hangman version 2.0 with actual stickman drawing with ears, feet, and hands
#Videos watched and comments read on https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman
#Idea of expanding by adding drawing of stickman
#Inspired by Chad Goldsworty in comments from PythonForBeginners.com link #1
# Resource used - http://openbookproject.net/thinkcs/python/english3e/functions.html
import random
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''','''
     +---+
    [O   |
    /|\  |
    / \  |
        ===''', '''
     +---+
    [O]  |
    /|\  |
    / \  |
        ===''','''
     +---+
    [O]  |
    /|\  |
   _/ \  |
        ===''', '''
     +---+
    [O]  |
    /|\  |
   _/ \_ |
        ===''','''
     +---+
    [O]  |
    /|\_ |
   _/ \_ |
        ===''', '''
     +---+
    [O]  |
   _/|\_ |
   _/ \_ |
        ===''']
words = {'Colors':'red orange yellow green blue white black brown'.split(),
        'Shapes':'square triangle rectangle circle pentagon octagon'.split(),
        'Fruits':'apple orange lemon lime grape cherry banana mango'.split(),
        'Animals':'bat bear giraffe cat tiger fish deer dog lion zebra'.split()}

def getRandomWord(wordDict):
    # Randomly select a key from the dictionary
    wordKey = random.choice(list(wordDict.keys()))
    # Randomly select a word from the key's list in the dictionary
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(HANGMAN_PICS, missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:')
    for letter in missedLetters:
        print('Missed letters: %s' % letter)
    print

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:  
        print(letter)
    print()

def getGuess(alreadyGuessed):
# Returns the letter the player entered.
#http://introtopython.org/while_input.html used for While loops,input
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # Function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')

difficulty = 'X'
#https://www.w3schools.com/python/python_while_loops.asp for loops info
while difficulty not in ['E', 'M', 'H']:
     print('Enter difficulty: E - Easy, M - Medium, H - Hard')
     difficulty = input().upper()
if difficulty == 'M':
     del HANGMAN_PICS[2]
     del HANGMAN_PICS[5]
if difficulty == 'H':
     del HANGMAN_PICS[3]
     del HANGMAN_PICS[1]
     del HANGMAN_PICS[4]
     del HANGMAN_PICS[2]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(HANGMAN_PICS, missedLetters, correctLetters, secretWord)

 # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

    # Check if the player has won
        foundAllLetters = True
#https://www.w3schools.com/python/ref_func_range.asp for range function
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(HANGMAN_PICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
