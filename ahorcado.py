import random
import os

def run():
    os.system("title <-----> AHORCADO: THE GAME <----->")
    IMAGES = ['''
        +----+
        |    |
        O    |
       /|\   |
       / \   |
             |
        =========''', '''
        +----+
        |    |
        O    |
       /|\   |
       /     |
             |
        =========''', '''
        +----+
        |    |
        O    |
       /|\   |
             |
             |
        =========''', '''
        +----+
        |    |
        O    |
       /|    |
             |
             |
        =========''', '''
        +----+
        |    |
        O    |
        |    |
             |
             |
        =========''', '''
        +----+
        |    |
        O    |
             |
             |
             |
        =========''', '''
        +----+
        |    |
             |
             |
             |
             |
        ========='''
    ]
    DB = [
        "PAPA",
        "YUCA",
        "MOLDAVIA",
        "ESTREMECER",
        "INJURIA",
        "OMNIPOTENTEM"
        "OMNISCIENS"
        "OMNIPRESENS"
        "SANTIAGO", #Yo XD
        "KOALA",
        "XD",
        "AZERBAIYAN",
        "CARACOL",
        "I AM THE STORM THAT IS APPROACHING"
    ]
    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 6

    while True:
        os.system("cls")
        for character in spaces:
            print(character, end = " ")
        print(IMAGES[attemps])
        letter = input("Inserta una letra ->").upper()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

        if not found:
            attemps -= 1

        if "_" not in spaces:
            print("\t\t* * Ganaste! :D * * ")
            break
            input()
        
        if attemps == 0:
            print("\t\t* * Perdiste! D: * * \nLa palabra era ->", word)
            break
            input()

if __name__ == '__main__':
    run()