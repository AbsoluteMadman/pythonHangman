#Python Hangman terminal game
from hashlib import new
import random

def game_title():  #Prints beautiful ascii art
    print("""    .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. | 
    | |   ______     | || |  ____  ____  | || |  _________   | || |  ____  ____  | || |     ____     | || | ____  _____  | |        _____ 
    | |  |_   __ \   | || | |_  _||_  _| | || | |  _   _  |  | || | |_   ||   _| | || |   .'    `.   | || ||_   \|_   _| | |        |/  |      
    | |    | |__) |  | || |   \ \  / /   | || | |_/ | | \_|  | || |   | |__| |   | || |  /  .--.  \  | || |  |   \ | |   | |        |   o     
    | |    |  ___/   | || |    \ \/ /    | || |     | |      | || |   |  __  |   | || |  | |    | |  | || |  | |\ \| |   | |        |  /|\     
    | |   _| |_      | || |    _|  |_    | || |    _| |_     | || |  _| |  | |_  | || |  \  `--'  /  | || | _| |_\   |_  | |        |  / \      
    | |  |_____|     | || |   |______|   | || |   |_____|    | || | |____||____| | || |   `.____.'   | || ||_____|\____| | |    ____|____    
    | |              | || |              | || |              | || |              | || |              | || |              | |   
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  
     '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   
     .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |
    | | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |
    | |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |
    | |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |
    | |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |
    | | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |
    | |              | || |              | || |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'""")

def get_word(category):  #Returns a random word from a specific list
    animals = ['cat', 'dog', 'giraffe', 'aardvark', 'lion', 'rat', 'frog', 'pig', 'cow', 'horse', 'whale', 'spider', 'squirrel', 'octopus', 'jellyfish', 'zebra', 'chimpanzee', 'raccoon', 'ocelot', 'platypus']
    cars = ['ford', 'ferarri', 'nissan', 'toyota', 'opel', 'skoda', 'volkswagen', 'mercedes', 'fiat', 'saab', 'lincoln', 'lexus', 'porsche', 'audi', 'bmw', 'renault', 'honda', 'lamborghini', 'koenigsegg', 'bugatti']
    countries = ['ireland', 'canada', 'ghana', 'france', 'russia', 'china', 'tibet', 'taiwan', 'japan', 'germany', 'spain', 'mexico', 'zimbabwe', 'israel', 'croatia', 'hungary', 'australia', 'sealand', 'greenland', 'sweden']
    programming_lang = ['python', 'java', 'perl', 'ruby', 'golang', 'javascript', 'bash', 'typescript', 'kotlin', 'sql', 'html', 'css', 'vba', 'rust']

    if category == 'a':
        word_num = random.randrange(0, len(animals) - 1)
        random_word = animals[word_num]

        return random_word

    elif category == 'b':
        word_num = random.randrange(0, len(cars) - 1)
        random_word = cars[word_num]
        
        return random_word

    elif category == 'c':
        word_num = random.randrange(0, len(countries) - 1)
        random_word = countries[word_num]
        
        return random_word

    elif category == 'd':
        word_num = random.randrange(0, len(programming_lang) - 1)
        random_word = programming_lang[word_num]
        
        return random_word

    else:
        exit 

    
def game_intro():
    print("Welcome to the game. Please choose an option.")
    print("[y] New game")
    print("[n] Quit")

    state = input("Enter your choice: ")
    if state == 'y' or state == 'Y':
        return True

    elif state == 'n' or state == 'N':
        return False


def get_game_word():
    print("Let's begin. Please choose a category:")
    print("[a] Animals")
    print("[b] Cars")
    print("[c] Countries")
    print("[d] Programming Languages")
    category = input("Select a category: ")
    game_word = get_word(category)
    #print(game_word)

    return game_word
    

def get_blanks(game_word):
    game_blanks = ""
    game_blanks_list = []

    for letter in game_word:
        game_blanks += " _ "
        game_blanks_list.append('_')
    
    return game_blanks, game_blanks_list


def update_blanks(new_letter, game_blanks, game_word): #finds the guessed letter in the game word and creates new blanks with the new letter
    game_blanks_string = ""

    for i in range(0, len(game_word)):
        if game_word[i] == new_letter:
            game_blanks[i] = new_letter

    for letter in game_blanks:
        game_blanks_string += letter + ' '

    return game_blanks_string


def word_checker(guesses, game_word):
    correct_counter = 0
    for letter in game_word:
        if letter in guesses:
            correct_counter +=1

    if len(game_word) == correct_counter:
        print("You Win")
        return True
    else:
        return False


def update_board(wrong_count):   #Updates the hangman board state
    hangman = ""

    if wrong_count == 0:
        hangman = """
        
            
            
            
             
             
        ____|____     
"""
    elif wrong_count == 1:
        hangman = """
        
            
        
            
            |
            |
        ____|____     
"""
    elif wrong_count == 2:
        hangman = """
        
            
            |
            |
            |  
            |  
        ____|____     
"""

    elif wrong_count == 3:
        hangman = """
        
            _____
            |
            |   
            |  
            |  
        ____|____     
"""

    elif wrong_count == 4:
        hangman = """
        
            _____
            |/  
            |   
            |  
            |  
        ____|____     
"""

    elif wrong_count == 5:
        hangman = """
        
            _____
            |/  
            |   o
            | 
            |  
        ____|____     
"""

    elif wrong_count == 6:
        hangman = """
        
            _____
            |/  
            |   o
            |   |
            |   
        ____|____     
"""

    elif wrong_count == 7:
        hangman = """
        
            _____
            |/  
            |   o
            |  /| 
            |   
        ____|____     
"""

    elif wrong_count == 8:
        hangman = """
        
            _____
            |/  
            |   o
            |  /|\ 
            |   
        ____|____     
"""

    elif wrong_count == 9:
        hangman = """
        
            _____
            |/  
            |   o
            |  /|\ 
            |  / 
        ____|____     
"""

    elif wrong_count == 10:
        hangman = """
        
            _____
            |/  
            |   o
            |  /|\ 
            |  / \ 
        ____|____     
"""

    elif wrong_count == 11:
        hangman = """
        Game over!!!
            _____
            |/  |
            |   o
            |  /|\ 
            |  / \ 
        ____|____     
"""
    return hangman


def game_logic():
    #Game while loop
    #print gamestate
    game_fail = False
    game_word = get_game_word()
    #print(game_word)
    win_num = len(game_word)
    blanks, blanks_list = get_blanks(game_word)
    print("Your word: " + blanks)
    wrong_count = 0
    correct_count = 0 #Instead of this, check the word after each letter guess. With this implementation, more than 1 letter occurring would not be counted.
    correct_list = []
    guesses = []
    #print(update_board(wrong_count))

    while game_fail == False:   #Main game loop
        input_check = 0

        while input_check == 0: #Loop for next input
            
            print(update_board(wrong_count))   #Updates the hangman board
            print("Incorrect guesses: " + str(guesses))           #Displays the incorrect letters guessed
            new_letter = input("Enter a letter: ")

            if new_letter.isalpha() == True & len(new_letter) == 1: #Basic input error checking, checks if single character and alphabet           
                correct_guess = game_word.find(new_letter) #checking if the letter is found in the word
                
                if correct_guess > -1:
                    correct_list.append(new_letter)
                    print("correct")
                    game_fail = word_checker(correct_list, game_word)
                    blanks = update_blanks(new_letter, blanks_list, game_word)
                    correct_count +=1
                    input_check +=1
                    
                else:
                        
                    if new_letter in guesses: #checks if letter is in guesses list
                        print("You already entered that letter. Try again.")

                    else: #if incorrect letter is guessed next hangman piece is added and board is updated
                        wrong_count +=1
                        input_check +=1
                        guesses.append(new_letter)
                        hangman = update_board(wrong_count)      
                        print(hangman)
                        if wrong_count >= 11:
                            game_fail = True
            
            else:
                print("Please enter a single alphabet character only.")

        print(update_blanks(new_letter, blanks_list, game_word))            
    
    if game_fail == True:
        print("\nThe word is: " + game_word)

        
#player_choice = True
game_title()
player_choice = game_intro()
while player_choice == True:
    
    game_logic()
    player_input = input("Would you like to play again? [y/n] ")
    if player_input == 'n':
        print("Goodbye.")
        player_choice = False
    elif player_input == 'y':
        player_choice == True
