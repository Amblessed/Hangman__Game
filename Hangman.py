# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


import string
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    myNew = True
    for char in secretWord:
        if char not in lettersGuessed:
            myNew = False
            break
    return myNew



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    string = ''
    for num in range(len(secretWord)):
        if secretWord[num] in lettersGuessed:
            string = string + secretWord[num]
        else:
            string = string + '_ '

    return string




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    newString = ''
    myString = string.ascii_lowercase
    for num in range(len(myString)):
        if myString[num] not in lettersGuessed:
            newString = newString + myString[num]
    return newString   
    

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
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    print("------------------")
    print("You have 8 guesses left.")
    print("Available letters:" + string.ascii_lowercase)
    myGuess = input("Please guess a letter:")
    myGuessLower = myGuess.lower()
    num = 8
    myS = []
    while num > 0:
        if myGuessLower in secretWord:
            if myGuessLower in myS:
                print('Oops! You\'ve already guessed that letter:' + getGuessedWord(secretWord,myS))
                print("------------------")
                print("You have " + str(num)  + " guesses left.")
                print("Available letters:" + getAvailableLetters(myS))
                myGuess = input("Please guess a letter:")
                myGuessLower = myGuess.lower()
                
            else:
                myS.append(myGuessLower)
                print("Good Guess:" + getGuessedWord(secretWord,myS))
                print("------------------")
                if isWordGuessed(secretWord,myS):
                    print("Congratulations, you won!")
                    break
                else:
                    print("You have " + str(num)  + " guesses left.")
                    print("Available letters:" + getAvailableLetters(myS))
                    myGuess = input("Please guess a letter:")
                    myGuessLower = myGuess.lower()
        else:         
            if myGuessLower not in myS:
                myS.append(myGuessLower)
                print("Oops!, That letter is not in my Word:" + getGuessedWord(secretWord,myS))
                print("------------------")
                num -= 1
                if num == 0:
                    print("Sorry, you ran out of guesses! The word was " +  secretWord) 
                    break
                print("You have "+ str(num) + " guesses left.")
                print("Available letters:" + getAvailableLetters(myS))
                myGuess = input("Please guess a letter:")
                myGuessLower = myGuess.lower()
                
            elif myGuessLower in myS:
                print('Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord,myS))
                print("------------------")
                print("You have "+ str(num) + " guesses left.")
                print("Available letters:" + getAvailableLetters(myS))
                myGuess = input("Please guess a letter:")
                myGuessLower = myGuess.lower()
                
##            else:
##                myS.append(myGuessLower)
##                num = num - 1
##                print("You have "+ str(num) + " guesses left.")
##                print("Available letters:" + getAvailableLetters(myS))
##                myGuess = input("Please guess a letter:")
##                myGuessLower = myGuess.lower()             
                
def main():
    #hangman("hangman")
    hangman("university")

main()                   
