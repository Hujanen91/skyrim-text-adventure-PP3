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



prompt()


while True:
    

    print("Scenario 1: The Peculiar Potion Peddler\n")
    print("While walking around in the town of Whiterun you encounter a peculiar alchemist selling bizarre potions. What do you do?\n")
    print("Option 1: Chug the Chuckle Elixir\nOption 2: Negotiate for a Guffaw Grenade\n")
    
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
            
       
