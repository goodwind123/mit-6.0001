# Problem Set 2, hangman.py
# Name: 
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
    for i in secret_word:
        if i not in letters_guessed:
            return False
    
    return True




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word=[]
    for i in secret_word:
        if i in letters_guessed:
            guessed_word.append(i)
        else:
            guessed_word.append('_')
    return ' '.join(guessed_word)
    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters=list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in available_letters:
            available_letters.remove(i)
            
    return ''.join(available_letters)
            
    
    

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
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    print('-------------')
    w=3    #warnings left
    g=6    #guesses left
    letters_guessed=[]
    while g>0:
        print('You have',g,'guesses left.')
        print('You have',w,'warnings left.')
        print('Available letters:',get_available_letters(letters_guessed))
        letter_guess=input('Please guess a letter:').lower()  #user guess
        if str.isalpha(letter_guess)==False:     #check if valid letter
            w-=1
            if w<=0:
                g-=1
                print('Oops! That is not a valid letter. You have no warnings left',g,'guesses left')
            else:
                print('Oops! That is not a valid letter. You now have',w,'warnings left:')
        if letter_guess in letters_guessed:
            if w<=0:
                g-=1
                print("Oops! You've already guessed that letter. You have no warnings left and",g,"guesses left")
                print('------------')
            else:
                w-=1
                print("Oops! You've already guessed that letter. You now have",w,"warnings left:")
                print('------------')
        else:
            letters_guessed.append(letter_guess)
            if letter_guess not in secret_word:
                print('Oops! That letter is not in my word:',get_guessed_word(secret_word,letters_guessed))
                if letter_guess in 'aeiou': #-2 guesses for vowels
                    g-=2
                else:
                    g-=1
            else:
                print('Good guess:',get_guessed_word(secret_word,letters_guessed))
                print('------------')
        if is_word_guessed(secret_word,letters_guessed) is True: #check if game is won
            print('Congratulations, you won!')
            total_score= g*len(secret_words)
            print('Your total score for this game is:',total_score)
            break
        
    print('Sorry, you ran out of guesses. The word was',secret_word)
#        
    
    



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
    '''
    my_word1=''.join(my_word.split(' '))
    if len(my_word1)!=len(other_word):
        return False
    
    for i in range(len(my_word1)):
        if  my_word1[i]!='_' and my_word1[i]!=other_word[i]:
            return False
        elif my_word1[i]==other_word[i] and my_word.count(my_word1[i]) != other_word.count(other_word[i]):
            return False
    
    return True
    # FILL IN YOUR CODE HERE AND DELETE "pass"




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word1=''.join(my_word.split(' '))
    possible_matches=[]
    for i in wordlist:
        if match_with_gaps(my_word1, i) is True:
            possible_matches.append(i)
    print(' '.join(possible_matches))



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
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    print('-------------')
    w=3    #warnings left
    g=6    #guesses left
    letters_guessed=[]
    while g>0:
        print('You have',g,'guesses left.')
        print('You have',w,'warnings left.')
        print('Available letters:',get_available_letters(letters_guessed))
        
        letter_guess=input('Please guess a letter:').lower()  #user guess
        
        if str.isalpha(letter_guess)==False and letter_guess!='*':     #check if valid letter
            w-=1
            if w<=0:
                g-=1
                print('Oops! That is not a valid letter. You have no warnings left',g,'guesses left')
            else:
                print('Oops! That is not a valid letter. You now have',w,'warnings left:')
        
        if letter_guess=='*':     #hints
            print('Possible word matches:')
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
            print('----------')
            
        if letter_guess in letters_guessed: #check if letter is guessed before
            if w<=0:
                g-=1
                print("Oops! You've already guessed that letter. You have no warnings left and",g,"guesses left")
                print('------------')
            else:
                w-=1
                print("Oops! You've already guessed that letter. You now have",w,"warnings left:")
                print('------------')
        else:
            letters_guessed.append(letter_guess)
            if letter_guess not in secret_word and letter_guess!='*':
                print('Oops! That letter is not in my word:',get_guessed_word(secret_word,letters_guessed))
                if letter_guess in 'aeiou': #-2 guesses for vowels
                    g-=2
                else:
                    g-=1
            elif letter_guess in secret_word:
                print('Good guess:',get_guessed_word(secret_word,letters_guessed))
                print('------------')
        if is_word_guessed(secret_word,letters_guessed) is True: #check if game is won
            print('Congratulations, you won!')
            total_score= g*len(secret_words)
            print('Your total score for this game is:',total_score)
            break
        
    print('Sorry, you ran out of guesses. The word was',secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
