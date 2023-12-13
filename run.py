import os
import sys
import pyfiglet

def clear():
    """
    Clear out the welcome message and start
    the game when the user presses enter.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def prompt():
    result = pyfiglet.figlet_format("Skyrim Word Adventure Game", font="digital")
    print(result+"A project created for code institute by Jennifer Hujanen\n\n")
    input("Press Enter to begin ...")
    clear()

    """Display starting game message"""
    print("\nHello Adventurer, please enter your name below:")
    player = input()
    print("\nWelcome " + player + ", our brave adventurer, to the land of Tamriel,\n" 
          "where dragons soar and sweetrolls are a cherished treasure.\n" 
          "As the chosen Dovakhiin, your quest is not to save the world\n" 
          "but to embark on a series of hilarious misadventures.\n")
    
    print(player + "! Are your ready?\n")
    input("Press Enter to continue ...")


prompt()
clear()


def scenarioOne():

    print("Scenario 1: The Peculiar Potion Peddler\n")
    print("While walking around in the town of Whiterun you encounter\n" 
          "a peculiar alchemist selling bizarre potions. What do you do?\n")
    print("Option 1: Chug the Chuckle Elixir?\n"
          "Option 2: Negotiate for a Guffaw Grenade?\n")

    userInput = input("Enter 1 or 2: ")

    while userInput not in {"1", "2"}:
        print("Please enter 1 or 2")
        userInput = input("Enter 1 or 2: ")
    clear()

    if userInput == "1":
        print("You entered option 1!\n"
              "Chug the Chuckle Elixir!")
        print(
            "You drink a potion labeled 'Chuckletonic',\n"
            "and suddenly everything becomes hilariously distorted.\n"
            "NPCs start telling punchlines,\n"
            "and you navigate the town with uncontrollable giggles.\n"
            "Hungry from all the laughter you head towards the tavern.\n"
        )

    elif userInput == "2":
        print("You entered option 2!\n")
        print(
            "You haggle with the alchemist for a laughter-inducing explosive.\n"
            "You accidentally toss it into a group of guards,\n"
            "who burst into fits of laughter,\n" 
            "allowing you to sneak into the local tavern unnoticed.\n"
        )
    input("Press enter to continue ...")
    clear()


def scenarioTwo():

    print("Scenario 2: The Enchanted Lute\n")
    print("After that weird encounter with the peculiar alchemist\n"
          "you turn around a corner and stumble upon a magical lute. What do you do?\n")
    print("Option 1: Play the Chicken Serenade?\n"
          "Option 2: Fus Ro Jam?\n")

    userInput = input("Enter 1 or 2: ")

    while userInput not in {"1", "2"}:
        print("Please enter 1 or 2")
        userInput = input("Enter 1 or 2: ")
    clear()

    if userInput == "1":
        print("You entered option 1!\n")
        print(
            "You strum a catchy tune dedicated to the town's chickens.\n"
            "The fowl flock to you,\n" 
            "forming a feathery entourage inside the small tavern.\n"
            "You gain the title 'Chicken chaser' and the chickens follow you\n"
            "as you leave Whiterun to search for your next adventure.\n"
        )

    elif userInput == "2":
        print("You entered option 2!\n")
        print(
            "You attempt to play the lute with the power of the Fus Ro Dah shout.\n"
            "The result is a magical musical explosion lifting\n"
            "the roof of the tavern and attracts a wandering bard.\n"
            "Impressed, the bard becomes your traveling companion,\n"
            "singing tales of your comedic prowess.\n"
            "'Toss a coin to your witcher'... oops, wrong universe.\n"
            "You and your new companion walk out the gates of Whiterun\n"
            "to look for a new quests to conquer.\n"
        )
    input("Press enter to continue ...")
    clear()


def scenarioThree():

    print("Scenario 3: The Jolly Mammoth Ride\n")
    print("After walking for a bit out in the plains of Whiterun,\n"
          "you spot what looks like a friendly giant herding mammoths.\n"
          "How do you approach this opportunity?\n")
    print("Option 1: Attempt a Mammoth Backflip?\n"
          "Option 2: Join the Mammoth Parade?\n")

    userInput = input("Enter 1 or 2: ")

    while userInput not in {"1", "2"}:
        print("Please enter 1 or 2")
        userInput = input("Enter 1 or 2: ")
    clear()

    if userInput == "1":
        print("You entered option 1!\n")
        print(
            "Inspired by the giants, you try a daring backflip onto a mammoth.\n"
            "Surprisingly, the mammoth enjoys the acrobatics but the giant not so much.\n"
            "You barely escaped with the help of your Fus Ro Dah shout.\n"
        )
        input("Press enter to continue ...")
        clear()        

    elif userInput == "2":
        print("You entered option 2!\n")
        print("You march alongside the giants, leading a mammoth parade through the plains\n"
              "and everyone's having a jolly good time.\n"
              "Or so you think until you're surprised attacked by the giant\n"
              "swinging his club making you fly like the dragon you are inside.\n")
        clear()
        print("Too bad Dovakhiin isn't invicible, you flew straight to oblivion!\n")
        restart = input("Press enter to restart the game ...")
        clear()
        prompt()


scenarioOne()
scenarioTwo()
scenarioThree()