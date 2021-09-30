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
    word_list = ['creature', 'faithful', 'crown', 'engine', 'divergent', 'gabby', 'cough', 'natural', 'tenuous', 'expensive', 'bucket', 'square', 'historical', 'unequaled', 'pizzas', 'trite', 'reaction', 'uppity', 'overwrought', 'waiting', 'rifle']
    animals = ['cat', 'dog', 'giraffe', 'aardvark', 'lion', 'rat', 'frog', 'pig', 'cow', 'horse', 'whale', 'spider', 'squirrel', 'octopus', 'jellyfish', 'zebra', 'chimpanzee', 'raccoon', 'ocelot', 'platypus']
    cars = ['ford', 'ferarri', 'nissan', 'toyota', 'opel', 'skoda', 'volkswagen', 'mercedes', 'fiat', 'saab', 'lincoln', 'lexus', 'porsche', 'audi', 'bmw', 'renault', 'honda', 'lamborghini', 'koenigsegg', 'bugatti']
    countries = ['ireland', 'canada', 'ghana', 'france', 'russia', 'china', 'tibet', 'taiwan', 'japan', 'germany', 'spain', 'mexico', 'zimbabwe', 'israel', 'croatia', 'hungary', 'australia', 'sealand', 'greenland', 'sweden']

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

    else:
        exit

    
def game_intro():
    print("Welcome to the game. Please choose an option.")
    print("[y] New game")
    print("[n] Quit")
    choice = input()
    print(choice)
    if choice == 'y':
        print("Let's begin. Please choose a category:")
        print("[a] Animals")
        print("[b] Cars")
        print("[c] Countries")
        category = input()
        game_word = get_word(category)
        #print(game_word)

        return game_word

    elif choice == 'n':
        print("Goodbye")

        #game exit
    

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
    game_word = game_intro()
    #print(game_word)
    win_num = len(game_word)
    blanks, blanks_list = get_blanks(game_word)
    print("Your word: " + blanks)
    game_fail = False
    wrong_count = 0
    correct_count = 0
    guesses = []
    #print(update_board(wrong_count))

    while game_fail == False:
        input_check = 0

        while input_check == 0:
            
            print(update_board(wrong_count)) 
            print("Incorrect guesses: " + str(guesses))           
            print("Enter a letter: ")
            new_letter = input()
            
            if len(new_letter) > 1:
                print("Only one letter at a time, you fatfingered sunofabitch! You're outta here!")
                exit
            
            correct_guess = game_word.find(new_letter)
            if correct_guess > -1:
                print("correct")
                blanks = update_blanks(new_letter, blanks_list, game_word)
                correct_count +=1
                input_check +=1
            
            else:
                
                if new_letter in guesses:
                    print("You already entered that letter. Try again.")

                else:
                    wrong_count +=1
                    guesses.append(new_letter)
                    hangman = update_board(wrong_count)      
                    print(hangman)
                
                if wrong_count >= 11:
                    game_fail = True
                input_check +=1
            print(update_blanks(new_letter, blanks_list, game_word))
            if correct_count == win_num:
                print("You win!!!")
                game_fail = True
    
    if game_fail == True:
        print("\nThe word is: " + game_word)
        
         
         
game_title()
game_logic()

