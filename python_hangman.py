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

    if category == 1:
        word_num = random.randrange(0, len(animals) - 1)
        random_word = animals[word_num]

    elif category == 2:
        word_num = random.randrange(0, len(cars) - 1)
        random_word = cars[word_num]

    elif category == 3:
        word_num = random.randrange(0, len(countries) - 1)
        random_word = countries[word_num]

    else:
        exit
    
    return random_word
    
def game_intro():
    print("Welcome to the game. Please choose an option.")
    print("[1] New game")
    print("[2] Quit")
    choice = input()
    print(choice)
    if choice == 1:
        print("Let's begin. Please choose a category:")
        print("[1] Animals")
        print("[2] Cars")
        print("[3] Countries")
        category = input()
        game_word = get_word(category)

    else:
        print("Goodbye")
        
        #game exit

def get_blanks(game_word):
    game_blanks = ""
      #Get the blank word
    for letter in game_word:
        game_blanks += " _ "
    
    return game_blanks

def update_blanks(new_letter, game_word): #finds the guessed letter in the game word and creates new blanks with the new letter
    game_blanks = []
    game_blanks_string = ""
    for letter in game_word:
        game_blanks.append('_ ')
    
    for i in range(0, len(game_word) - 1):
        if game_word[i] == new_letter:
            game_blanks[i] = new_letter + ' '

    for letter in game_blanks:
        game_blanks_string += letter

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


    



def game_logic(game_blanks, game_word):
    #Game while loop
    #print gamestate
    game_fail = False
    wrong_count = 0
    while game_fail == False:
        print("Enter a letter: ")
        new_letter = input()

        for letter in game_word:
            if letter == new_letter:
                print("Correct!")
                #update_blanks(new_letter, game_blanks, game_word)
                #draw new board
                #print new blanks
            else:
                print("Wrong answer!")
                wrong_count +=1
                #update_board(wrong_count)
         
""" game_title()
#game_intro()
new_word = get_word(2)
print(new_word) """


x = update_board(5)
print(x)