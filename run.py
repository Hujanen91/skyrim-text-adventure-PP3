# import pyfiglet module 
import pyfiglet 
  
result = pyfiglet.figlet_format("Skyrim  Word  Adventure  Game", font = "digital" ) 
print(result + "A project created for code institute by Jennifer Hujanen\n\n")

def prompt():
    """Display starting game message"""
    print(
        "Welcome to a funny word adventure game that will take place in Whiterun in the world of Skyrim"
        )

    input("Press 'enter' to continue ...")


prompt()