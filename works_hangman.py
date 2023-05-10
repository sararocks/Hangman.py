# Problem Set 2, hangman.py
# Name: Sara Jane Mildenstein!!!! 
# Collaborators:
# Time spent: 

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
 
    # are all the letters in secret word in letters guessed  
    # we have already defind secret word and letters guessed 
    # 1. turn secret word into a list of letters? 
    # 2. compare the list of letters to the letters that are guessed 
    # 3. OR do i do a stack? which is maybe the same as a dictionary? 
    
    # FROM CASEY - check each letter in the word, and if those letters are not in letters guessed, letter has not been guessed yet 
    # check if any letter in the word is in the guessed list 
    
    for letter in secret_word: # a string is a list of characters that we can already loop over!
        if letter not in letters_guessed: # we use in or not in to see if a list contains a thing, also we don't need an else clause because we are trying to find reasons to quit, not reasons to keep going 
            return False
    return True # if we have gotten here then all letters in the secret word are found in the guessed list

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    
    # short story: make a temporary string which is empty to start with. 2 - look through all of the letters in the secret word. 3 - if the letter is in the guessed letters, stick the letter on the end of the temporary string. 4 - if letter is not in guessed letters, stick a space and an underscore 5 - then we return the temporary string 
    
    temp_str = ""
    for letter in secret_word: 
        if letter in letters_guessed:
           temp_str = temp_str + letter + ' '
        if letter not in letters_guessed:
            temp_str = temp_str + '_ '
    
    # print(temp_str) # just for checking purposes
    return temp_str
    
   
          
    
    
    pass



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    
    remaining_letters = "abcdefghijklmnopqrstuvwxyz"
    
    for letter in letters_guessed: 
        remaining_letters = remaining_letters.replace(letter, '')
    # print(remaining_letters) 
    return remaining_letters
    
    
    # now it works yay

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
   
    #### 3/13
  
    letters_in_word = len(secret_word)
    letters_guessed_sofar = []
    number_warnings = 3
    guesses_remaining = 6  
    print("Welcome to the game of hangman!")
    print(f'I am thinking of a word that is {letters_in_word} letters long.') 
    print(f'You have {number_warnings} warnings left.')    
    
    
    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed_sofar):
        print("------------")   
        print(f'You have {guesses_remaining} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed_sofar)}')
        user_guess_up_or_low = input("Please guess a letter: ") #assignment   
        user_guess = user_guess_up_or_low.lower()
                   
        if user_guess in letters_guessed_sofar:
            if number_warnings == 0:
                guesses_remaining -= 1
                print(f"Oops! You've already guessed that letter, and you are out of warnings. You will lose a guess, and you now have {guesses_remaining} guesses left: {get_guessed_word(secret_word, letters_guessed_sofar)}")
            else:    
                number_warnings -= 1
                print(f"Oops! You've already guessed that letter. You now have {number_warnings} warnings: {get_guessed_word(secret_word, letters_guessed_sofar)}")
                
        if user_guess not in secret_word and user_guess.isalpha() == True: 
            print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed_sofar)}')
            letters_guessed_sofar.append(user_guess)
            if user_guess == 'a' or user_guess == 'e' or user_guess == 'i' or user_guess == 'o' or user_guess == 'u':
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1 
                
        if user_guess.isalpha() == False:
            if number_warnings == 0:
                guesses_remaining -= 1
                print(f"Oops! That is not a valid letter, and you are out of warnings. You will lose a guess, and you now have {guesses_remaining} guesses left: {get_guessed_word(secret_word, letters_guessed_sofar)}")
            else:
                number_warnings -= 1
                print(f'Oops! That is not a valid letter. You have {number_warnings} warnings left: {get_guessed_word(secret_word, letters_guessed_sofar)}')                         
        if user_guess in secret_word:
            letters_guessed_sofar.append(user_guess)
            print(f'Good guess: {get_guessed_word(secret_word, letters_guessed_sofar)}')

        if is_word_guessed(secret_word, letters_guessed_sofar):
            print("YOU WIN!")
            print(f'Your total score for this game is: {guesses_remaining* len(secret_word)}') # need to count only unique letters 
            
        if guesses_remaining == 0:
            print(f'Sorry, you ran out of guesses. The word was {secret_word}.')  
        
   

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
        
    SARA WORDS - compare the word user has guessed so far with all the other words in the loaded list that contain those same letters in the same order. 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    my_word = get_guessed_word(secret_word, letters_guessed_sofar)
    other_word = word that has the same letters in the same placement --- word in wordlist? - call one word in the list? 
    
    other_word = choose_word(wordlist) #will this go through every word? 
    wordlist = load_words()
    wordlist = line.split()
    # this is from above - not sure which to use
  
  
    if my_word = # same letters same placement of other_word:
        return True 
        
    else:
        return False
    
    # we need it to go through ALL of the words though...does the above do that? 
    
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    my_word = get_guessed_word(secret_word, letters_guessed_sofar) # ok having a meta moment, isn't this just saying that the thing is already the thing...?
    
    
    
    
    
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    if user_guess == *:
        print(f'Possible word matches are:
            { #the functions we need to call }
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)

    # if you want to test functions 3 4 and 5 from the top
    
    # secret_word = 'apple' 
    # letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
    # assert is_word_guessed(secret_word, letters_guessed) == False 
    # assert get_guessed_word(secret_word, letters_guessed) == '_ pp_ e'
    # assert get_available_letters(letters_guessed) == 'abcdfghjlmnoqtuvwxyz'


    
    # secret_word = 'apple' 
    # letters_guessed = ['a', 'p', 'l', 'e', 's'] 
    # assert is_word_guessed(secret_word, letters_guessed) == True
    # assert get_guessed_word(secret_word, letters_guessed) == 'apple'
    # assert get_available_letters(letters_guessed) == 'bcdfghijkmnoqrtuvwxyz'
    
    # print("All tests passed!")
    
    
