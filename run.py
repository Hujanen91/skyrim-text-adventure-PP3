import os
import sys
# import pyfiglet module 
import pyfiglet

  
result = pyfiglet.figlet_format("Skyrim  Word  Adventure  Game", font = "digital" ) 
print(result + "A project created for code institute by Jennifer Hujanen\n\n")

def prompt():
    """Display starting game message"""
    print(
        "Welcome to a funny word adventure game that will take place in Whiterun in the world of Skyrim"
        )
    
    print("Hello Adventurer, what is your name?")
    player = input()
    print("\nWelcome\t" + player+"! Are your ready?\n")
    input("Press Enter to begin ...")


def clear():
    """
    Clear out the welcome message and start the game when the user presses enter.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

prompt()
clear()

def scenarioOne():
    #clear()

    print("Scenario 1: The Peculiar Potion Peddler\n")
    print("While walking around in the town of Whiterun you encounter a peculiar alchemist selling bizarre potions. What do you do?\n")
    print("Option 1: Chug the Chuckle Elixir?\nOption 2: Negotiate for a Guffaw Grenade?\n")
    
    userInput = input("Enter 1 or 2: ")
    
    while userInput not in {"1", "2"}:
        print("Please enter 1 or 2")
        userInput = input("Enter 1 or 2: ")
       
    if userInput == "1":
        print("You entered option 1!\n")
        print(
            "You drink a potion labeled 'Chuckletonic', and suddenly everything becomes hilariously distorted.\n"
            "NPCs start telling punchlines, and you navigate the town with uncontrollable giggles.\n"
            "Hungry from all the laughter you head towards the tavern."
        )
        
    elif userInput == "2":
        print("You entered option 2!\n")
        print(
            "You haggle with the alchemist for a laughter-inducing explosive.\n" 
            "You accidentally toss it into a group of guards, who burst into fits of laughter, allowing you to sneak into the local tavern unnoticed."
        )
    input("Press enter to continue ...")
    clear()
    

def scenarioTwo():
    #clear()

    print("Scenario 2: The Enchanted Lute\n")
    print("After that weird encounter with the peculiar alchemist you turn around a corner and stumble upon a magical lute. What do you do?\n")
    print("Option 1: Play the Chicken Serenade?\nOption 2: Fus Ro Jam?\n")
    
    userInput = input("Enter 1 or 2: ")
    
    while userInput not in {"1", "2"}:
        print("Please enter 1 or 2")
        userInput = input("Enter 1 or 2: ")
       
    if userInput == "1":
        print("You entered option 1!\n")
        print(
            "You strum a catchy tune dedicated to the town's chickens.\n" 
            "The fowl flock to you, forming a feathery entourage inside the small tavern.\n"
            "You gain the title 'Clucker's Maestro.'"
        )
        
    elif userInput == "2":
        print("You entered option 2!\n")
        print(
            "You attempt to play the lute with the power of the Fus Ro Dah shout.\n"
            "The result is a magical musical explosion lifting the roof of the tavern and attracts a wandering bard.\n"
            "Impressed, the bard becomes your traveling companion, singing tales of your comedic prowess.\n"
            "'Toss a coin to your witcher'... oops, wrong universe."
        )
    input("Press enter to continue ...")

def scenarioThree():
    #clear()

    print("Scenario 2: The Enchanted Lute\n")
    print("After that weird encounter with the peculiar alchemist you turn around a corner and stumble upon a magical lute. What do you do?\n")
    print("Option 1: Play the Chicken Serenade?\nOption 2: Fus Ro Jam?\n")
    
    userInput = input("Enter 1 or 2: ")
    
    while userInput not in {"1", "2"}:
        print("Please enter 1 or 2")
        userInput = input("Enter 1 or 2: ")
       
    if userInput == "1":
        print("You entered option 1!\n")
        print(
            "You strum a catchy tune dedicated to the town's chickens.\n" 
            "The fowl flock to you, forming a feathery entourage inside the small tavern.\n"
            "You gain the title 'Clucker's Maestro.'"
        )
        
    elif userInput == "2":
        print("You entered option 2!\n")
        print(
            "You attempt to play the lute with the power of the Fus Ro Dah shout.\n"
            "The result is a magical musical explosion lifting the roof of the tavern and attracts a wandering bard.\n"
            "Impressed, the bard becomes your traveling companion, singing tales of your comedic prowess.\n"
            "'Toss a coin to your witcher'... oops, wrong universe."
        )
    input("Press enter to continue ...")
    
        
scenarioOne()
scenarioTwo()
scenarioThree()