# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    neededLetters = []
    counter = 0
    
    #base case where no letters have been guessed
    if len(lettersGuessed) == 0:
        return False
        
    #create a list of unique characters in the guessed word
    for y in secretWord:
        if y not in neededLetters:
            neededLetters.append(y)
    #check if the guessed chars match all unique characters
    for char in lettersGuessed:
        if char in neededLetters:
            counter += 1
    #if all the unique letters have been found return True else False
    if counter >= len(neededLetters):
        return True
    else:
        return False
 


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
   
    word = ''
    
    
   #want to iterate over each value in secretWord and if in Guessed fill in 
    for char in secretWord:
        if char in lettersGuessed:
            word += char
        else:
            word += '_ '
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    
    letters = string.ascii_lowercase
    lettersAvailable = ''
    
    #for each character in the alphabet check if guessed and if not add to new string
    for char in letters:
        if char not in lettersGuessed:
            lettersAvailable += char
    return lettersAvailable
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is ', len(secretWord), ' letters long')
    print ('---------------')
    
    guesses = 0
    lettersGuessed = []
    
    while guesses < 8:
        print ('You have ', 8-guesses, ' guesses left')
        print ('Available letters: ', getAvailableLetters(lettersGuessed))
        
        # take an input letter, convert it to lower case and add the character to list
        
        letterinput = input('Please guess a letter: ')
        lowerletterinput = letterinput.lower()
        
        #CASE1: if input letter is a repeat 
        if lowerletterinput in lettersGuessed:
            print ("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        
        #CASE2: if input letter is new and in the secretWOrd
        if lowerletterinput not in lettersGuessed and lowerletterinput in secretWord:
            lettersGuessed.append(lowerletterinput)
            print ('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            
        #CASE 3: if input letter is new and not in the secretWord
        if lowerletterinput not in lettersGuessed and lowerletterinput not in secretWord:
            lettersGuessed.append(lowerletterinput)
            guesses += 1
            print ('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
        
        print ('---------------')
        
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            return
    print('Sorry, you ran out of guesses. The word was ', secretWord, '.')
    return 
            
        
    
    




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
