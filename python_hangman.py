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
    animals = ['cat', 'dog', 'giraffe', 'aardvark', 'lion', 'rat', 'frog', 'pig', 'cow', 'horse', 'whale', 'spider', 'squirrel', 'octopus', 'jellyfish', 'zebra']
    cars = ['ford', 'ferarri', 'nissan', 'toyota', 'opel', 'skoda', 'volkswagen', 'mercedes', 'fiat', 'saab', 'lincoln', 'lexus', 'porsche', 'audi', 'bmw', 'renault', 'honda']
    countries = ['ireland', 'canada', 'ghana', 'france', 'russia', 'china', 'tibet', 'taiwan', 'japan', 'germany', 'spain', 'mexico', 'zimbabwe', 'israel', 'croatia']

    if category == 1:
        word_num = random.randrange(0, len(animals))
        random_word = animals[word_num]

    elif category == 2:
        word_num = random.randrange(0, len(cars))
        random_word = cars[word_num]

    elif category == 3:
        word_num = random.randrange(0, len(countries))
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

def update_blanks(new_letter, game_blanks, game_word):
    updated_blanks = ""
    #append game_blanks with new letter in x position
    return updated_blanks



def game_logic(game_blanks, game_word):
    #Game while loop
    #print gamestate
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
            #update_board()
         
game_title()
#game_intro()
new_word = get_word(3)
print(new_word)
