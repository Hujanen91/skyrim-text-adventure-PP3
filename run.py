import os
import sys
import pyfiglet
import random
from riddles import RIDDLES

"""
Clear out the welcome message and start
the game when the user presses enter.
"""
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

"""
Prompt the welcome message and ask the player for a name.
"""
def prompt():
    result = pyfiglet.figlet_format("Skyrim Word Adventure Game", font="digital")
    print(result+"A project created for code institute by Jennifer Hujanen\n\n")
    input("Press Enter to begin ...")
    clear()

    """Display starting game message"""
    print("\nHello Adventurer, please enter your name below:")

    """
    Ask the player for a name. The name is required and needs to
    be only letters and at least 3 letters long.
    """
    while True:
        try:
            name = input("")
            if not name.isalpha():
                print("Sorry, your name should only contain letters")
            elif len(name) < 3:
                print("Sorry, your name needs to be more then 3 letters")
            else:
                clear()     
                print("\nWelcome " + name + ", our brave adventurer, to the land of Tamriel,\n" 
                    "where dragons soar and sweetrolls are a cherished treasure.\n" 
                    "As the chosen dragonborn, your quest is not to save the world\n" 
                    "but to embark on a series of hilarious misadventures.\n")
                print(name + "! Are your ready?")
                input("\nPress Enter to continue ...")
                break
        except Exception as e:
            print(f"An error occurred: {e}")


def restart_program():
    """
    Restarts the current program.
    """
    python = sys.executable
    os.execl(python, python, * sys.argv)
    restart_program()


prompt()
# Clear out welcome message:
clear()


def scenarioOne():

    print("Scenario 1: The Peculiar Potion Peddler")
    print("\nWhile walking around in the town of Whiterun you encounter\n" 
        "a peculiar alchemist selling bizarre potions. What do you do?\n")
    print("Option 1: Chug the Chuckle Elixir?\n"
        "Option 2: Negotiate for a Guffaw Grenade?\n")

    userInput = input("Enter 1 or 2: ")

    while userInput not in {"1", "2"}:
        print("Please enter 1 or 2")
        userInput = input("Enter 1 or 2: ")
    clear()

    if userInput == "1":
        print("You entered option 1:\n"
            "Chug the Chuckle Elixir!\n")
        print(
            "\nYou drink a potion labeled 'Chuckletonic',\n"
            "and suddenly everything becomes hilariously distorted.\n"
            "NPCs start telling punchlines,\n"
            "and you navigate the town with uncontrollable giggles.\n"
            "Hungry from all the laughter you head towards the tavern.\n"
            )

    elif userInput == "2":
        print("You entered option 2:\n"
            "Negotiate for a Guffaw Grenade\n")
        print(
            "\nYou haggle with the alchemist for a laughter-inducing explosive.\n"
            "You accidentally toss it into a group of guards,\n"
            "who burst into fits of laughter,\n" 
            "allowing you to sneak into the local tavern unnoticed.\n"
            )
    input("Press enter to continue ...")
    clear()
scenarioOne()


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
        print("You entered option 1:\n"
            "Play the Chicken Serenade!\n")
        print(
            "You strum a catchy tune dedicated to the town's chickens.\n"
            "The fowl flock to you,\n" 
            "forming a feathery entourage inside the small tavern.\n"
            "You gain the title 'Chicken chaser' and the chickens follow you\n"
            "as you leave Whiterun to search for your next adventure.\n"
            "But before you could leave a bard decides to follow along\n"
            "because a 'Chicken chaser' seems like a perfect adventurer to write\n"
            "songs about\n"
            )

    elif userInput == "2":
        print("You entered option 2:\n"
            "Fus Ro Jam\n")
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
scenarioTwo()


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
        print("You entered option 1:\n"
            "Attempt a Mammoth Backflip!\n")
        print(
            "Inspired by the giants, you try a daring backflip onto a mammoth.\n"
            "Surprisingly, the mammoth enjoys the acrobatics but the giant not so much.\n"
            "You barely escaped with the help of your Fus Ro Dah shout\n"
            "and the bard is right behind you singing songs about what just happened\n"
            )
        input("Press enter to continue ...")
        clear()

    elif userInput == "2":
        print("You entered option 2:\n"
            "Join the Mammoth Parade!\n")
        print("You march alongside the giants, leading a mammoth parade through the plains\n"
            "and everyone's having a jolly good time.\n"
            "Or so you think until you're surprised attacked by the giant\n"
            "swinging his club making you fly like the dragon you are inside.\n")
        clear()
        print("Too bad Dovakhiin isn't invicible, you flew straight to oblivion!\n")
        input("Press enter to restart ...")
        clear()
        restart_program()
        
scenarioThree()               


def scenarioFour():

    print("Scenario 4: The Whimsical Werewolf\n")
    print("You got tired of your companion Bard singing your ears off\n"
          "so not short after your travels outside of Whiterun you\n"
          "Fos-Ro-Dah his lute into oblivion and the Bard left.\n"
          "As nightfall enters and the moon rises, you feel\n"
          "the transformation coming on. What's your approach?\n")
    print("Option 1: Embrace the Dance of the Werewolf?\n"
          "Option 2: Attempt Werewolf Stand-Up Comedy?\n")

    userInput = input("Enter 1 or 2: ")

    while userInput not in {"1", "2"}:
        print("Please enter 1 or 2")
        userInput = input("Enter 1 or 2: ")
    clear()

    if userInput == "1":
        print("You entered option 1:\n"
              "Embrace the Dance of the Werewolf!\n")
        print(
            "You transform and start a moonlit dance party with other werewolves.\n"
            "The locals join in, and you become the talk of the town as the\n"
            "'Howling Dance Champion.' Morning comes and you decide to contune further\n"
            "along on this weird and random journey.\n"
            )

    elif userInput == "2":
        print("You entered option 2:\n"
              "Attempt Werewolf Stand-Up Comedy!\n")
        print(
            "You try telling jokes in your werewolf form,\n"
            "but the audience finds your delivery too 'howl-arious'.\n"
            "The Jarl appoints you as the official court jester.\n"
            "You tell the Jarl thanks but no thanks, you're only\n"
            "interest right now is continuing on with your journey\n"
            )
    input("Press enter to continue ...")
    clear()
scenarioFour()


def scenarioFive():

    print("Scenario 5: The Ancient Tomb of Laughter\n")
    print("You're joined by your 'always-in-my-way' trusty companion\n"
          "Lydia and the two of you continue on your journy.\n"
          "You stumble upon an ancient tomb and start exploring it.\n"
          "Deep in the tomb you encounter a ghostly figure.\n"
          "How do you approach the situation?\n")
    print("Option 1: The Ghost Whisperer?\n"
          "Option 2: Startle Stand-Up?\n")

    userInput = input("Enter 1 or 2: ")

    while userInput not in {"1", "2"}:
        print("Please enter 1 or 2")
        userInput = input("Enter 1 or 2: ")
    clear()

    if userInput == "1":
        print("You entered option 1:\n"
              "The Ghost Whisperer!\n")
        print(
            "You engage the ghost in a friendly conversation,\n"
            "discovering it's a bored bard from ancient times.\n"
            "You form a spectral band and will later tour Skyrim's crypts\n"
            "and spreading spooky merriment.\n"
            "But for now you continue back out from the crypt\n"
            "with Lydia right behind you\n"
            )

    elif userInput == "2":
        print("You entered option 2:\n"
              "Startle Stand-Up!\n")
        print(
            "You try to tell ghost-themed jokes,\n"
            "inadvertently making the ghost laugh so hard it disappears.\n"
            "The tomb later becomes a popular comedy club for ghosts,\n"
            "and you'll gain a legion of spectral fans.\n"
            "But for now you'll continue on your journey with Lyda\n"
            "right behind you. You decide to leave the crypt to continue\n"
            "your travels\n"
            )
    input("Press enter to continue ...")
    clear()
scenarioFive()

def scenarioSix():
    riddle_index = random.randint(0, len(RIDDLES) - 1)
    selected_riddle = RIDDLES[riddle_index]

    print("Scenario 6: Cicero the ever so annoying jester\n")
    print("Right before leaving the crypt Cicero, the eccentric and annoying\n"
          "jester appears. He has sealed off the entrance and wont let you pass until you solve a riddle\n"
          "'Ah Adventurer! Cicero sees you approach, yes, yes.\n"
          "But to pass, a challenge awaits, a riddle to tease that clever mind of yours.\n"
          "Oh, and a delightful one! Listen carefully, my dear friend:\n\n")
    
    print(selected_riddle["riddle"])

    for i, option in enumerate(selected_riddle["options"], start=1):
        print(f"Option {i}: {option}")

    user_input = input(f"Enter the number of your answer (1-{len(selected_riddle['options'])}): ")

    while not user_input.isdigit() or int(user_input) not in range(1, len(selected_riddle['options']) + 1):
        print(f"Please enter a valid option (1-{len(selected_riddle['options'])}): ")
        user_input = input(f"Enter the number of your answer (1-{len(selected_riddle['options'])}): \n")

    selected_option = selected_riddle["options"][int(user_input) - 1]

    if selected_option == selected_riddle["correct_answer"]:
        print("\nCicero applauds your wit! You may pass.")
        clear()
        print("Congratulations! You, the dragonborn of Skyrim,\n"
              "managed to solve the riddle and continue on with your journey.\n"
              "You have turned the harsh world of Tamriel into a realm of laughter and joy.\n"
              "The people sing songs of your whimsical exploits,\n"
              "and you became the legendary hero of humor.\n"
              "May your journey continue to be filled with hilarity and merriment!")
        input("Press enter to restart ...")
        clear()
        restart_program()
    else:
        print("Alas! Cicero cackles with mockery.\n" 
             f"The correct answer was {selected_riddle['correct_answer']}.")
        print("\nCicero closes the exit and you are forced back down in to the tomb.")
        input("Press enter to restart ...")
        clear()
        restart_program()

scenarioSix()

    