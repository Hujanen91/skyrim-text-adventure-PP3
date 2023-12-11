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
    print("Welcome\t" + player+"! Are your ready to begin?\n")
    input("Press Enter to begin ...")

prompt()

def clear():
    """
    Clear out the welcome message and start the game when the user presses enter.
    """