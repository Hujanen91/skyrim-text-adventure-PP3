import os
import sys
import pyfiglet
import random
import colorama
from colorama import Fore, Back, Style
from riddles import RIDDLES
colorama.init(autoreset=True)


def clear():
    """
    Clear out the welcome message and start
    the game when the user presses enter.
    """

    os.system('cls' if os.name == 'nt' else 'clear')


def section_border():
    """ Sets a border to call when needed for better visuals """
    print("~" * 65)


def prompt():
    """
    Prompt the welcome message and ask the player for a name.
    """
    result = pyfiglet.figlet_format("Skyrim Word Adventure Game",
                                    font="digital")
    print(result+"A project created for code institute by "
          "Jennifer Hujanen\n\n")
    input(Fore.YELLOW + "Press Enter to begin ...")
    clear()

    """Display starting game message"""
    print()
    section_border()
    print("Hello Adventurer, please enter your name below:")
    section_border()

    """
    Ask the player for a name. The name is required and needs to
    be only letters and at least 3 letters long.
    """
    while True:
        try:
            name = input("")

            if not name.isalpha():
                print(Fore.RED +
                      "Sorry, your name should only contain letters")
                section_border()
            elif len(name) < 3:
                print(Fore.RED +
                      "Sorry, your name needs to be more then 3 letters")
                section_border()

            else:
                clear()
                section_border()
                print(
                      "\nWelcome " + name + ", our brave adventurer,\n"
                      "to the land of Tamriel, where dragons\n"
                      "soar and sweetrolls are a cherished treasure.\n"
                      "As the chosen dragonborn, your quest is \n"
                      "not to save the world but to embark on\n"
                      "a series of hilarious misadventures.\n"
                     )
                section_border()
                print(name + "! Are your ready?")
                section_border()
                input(Fore.YELLOW + "\nPress Enter to continue ..."
                      + Fore.RESET)
                break
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}")


def restart_program():
    """ Restarts the current program """
    python = sys.executable
    os.execl(python, python, * sys.argv)
    restart_program()


# Call the prompt function
prompt()
# Clear out welcome message:
clear()


def scenarioOne():
    """
    Scenario one to six that contains the game itself.
    It will print scenarios and different options for different scenarios.
    In 2 of the scenarios the player will either die or loose.
    """
    section_border()
    print(Fore.YELLOW + "Scenario 1: The Peculiar Potion Peddler" + Fore.RESET)
    section_border()
    print(
          "\nWhile walking around in the town of Whiterun you encounter\n"
          "a peculiar alchemist selling bizarre potions. What do you do?\n"
         )
    section_border()
    print(Fore.BLUE + "Option 1: Chug the Chuckle Elixir?\n"
          "Option 2: Negotiate for a Guffaw Grenade?\n")

    userInput = input("Enter 1 or 2: ")

    while userInput not in {"1", "2"}:
        print("Please enter 1 or 2")
        userInput = input("Enter 1 or 2: ")
    clear()

    if userInput == "1":
        section_border()
        print(Fore.BLUE + "You entered option 1:"
              "\nChug the Chuckle Elixir!")
        section_border()
        print(
              "\nYou drink a potion labeled 'Chuckletonic',\n"
              "and suddenly everything becomes hilariously distorted.\n"
              "NPCs start telling punchlines,\n"
              "and you navigate the town with uncontrollable giggles.\n"
              "Hungry from all the laughter you head towards the tavern.\n"
             )
        section_border()

    elif userInput == "2":
        section_border()
        print(Fore.BLUE + "You entered option 2:"
              "\nNegotiate for a Guffaw Grenade")
        section_border()
        print(
              "\nYou haggle with the alchemist for a\n"
              "laughter-inducing explosive.\n"
              "You accidentally toss it into a group of guards,\n"
              "who burst into fits of laughter,\n"
              "allowing you to sneak into the local tavern unnoticed.\n"
             )
        section_border()
    input(Fore.YELLOW + "Press enter to continue ..." + Fore.RESET)
    clear()


scenarioOne()


def scenarioTwo():
    section_border()
    print(Fore.YELLOW + "Scenario 2: The Enchanted Lute" + Fore.RESET)
    section_border()
    print(
          "\nAfter that weird encounter with the peculiar alchemist\n"
          "you turn around a corner in the tavern\n"
          "and stumble upon a magical lute.\n"
          "What do you do?\n"
         )
    section_border()
    print(Fore.BLUE + "Option 1: Play the Chicken Serenade?\n"
          "Option 2: Fus Ro Jam?\n")

    userInput = input("Enter 1 or 2: ")

    while userInput not in {"1", "2"}:
        print("Please enter 1 or 2")
        userInput = input("Enter 1 or 2: ")
    clear()

    if userInput == "1":
        section_border()
        print(Fore.BLUE + "You entered option 1:"
              "\nPlay the Chicken Serenade!")
        section_border()
        print(
              "\nYou strum a catchy tune dedicated to the town's chickens.\n"
              "The fowl flock to you,\n"
              "forming a feathery entourage inside the small tavern.\n"
              "You gain the title 'Chicken chaser' and the chickens follow\n"
              "you as you leave Whiterun to search for your next adventure.\n"
              "But before you could leave a bard decides to follow along\n"
              "because a 'Chicken chaser' seems like a perfect adventurer\n"
              "to write songs about\n"
             )
        section_border()

    elif userInput == "2":
        section_border()
        print(Fore.BLUE + "You entered option 2:"
              "\nFus Ro Jam")
        section_border()
        print(
              "\nYou attempt to play the lute with the power\n"
              "of the Fus Ro Dah shout.\n"
              "The result is a magical musical explosion lifting\n"
              "the roof of the tavern and attracts a wandering bard.\n"
              "Impressed, the bard becomes your traveling companion,\n"
              "singing tales of your comedic prowess.\n"
              "'Toss a coin to your witcher'... oops, wrong universe.\n"
              "You and your new companion walk out the gates of Whiterun\n"
              "to look for a new quests to conquer.\n"
             )
        section_border()
    input(Fore.YELLOW + "Press enter to continue ..." + Fore.RESET)
    clear()


scenarioTwo()


def scenarioThree():
    section_border()
    print(Fore.YELLOW + "Scenario 3: The Jolly Mammoth Ride" + Fore.RESET)
    section_border()
    print(
          "\nAfter walking for a bit out in the plains of Whiterun,\n"
          "you spot what looks like a friendly giant herding mammoths.\n"
          "How do you approach this opportunity?\n"
         )
    section_border()
    print(Fore.BLUE + "Option 1: Attempt a Mammoth Backflip?\n"
          "Option 2: Join the Mammoth Parade?\n")

    userInput = input("Enter 1 or 2: ")

    while userInput not in {"1", "2"}:
        print("Please enter 1 or 2")
        userInput = input("Enter 1 or 2: ")
    clear()

    if userInput == "1":
        section_border()
        print(Fore.BLUE + "You entered option 1:"
              "\nAttempt a Mammoth Backflip!")
        section_border()
        print(
              "\nInspired by the giants, you try a daring\n"
              "backflip onto a mammoth.\n"
              "Surprisingly, the mammoth enjoys the acrobatics\n"
              "but the giant not so much.\n"
              "You barely escaped with the help of your Fus Ro Dah shout\n"
              "and the bard is right behind you\n"
              "singing songs about what just happened\n"
             )
        section_border()
        input(Fore.YELLOW + "Press enter to continue ..." + Fore.RESET)
        clear()

    elif userInput == "2":
        section_border()
        print(Fore.BLUE + "You entered option 2:"
              "\nJoin the Mammoth Parade!")
        section_border()
        print(
              "\nYou march alongside the giants,\n"
              "leading a mammoth parade through the plains\n"
              "and everyone's having a jolly good time.\n"
              "Or so you think until you're surprised attacked by the giant\n"
              "swinging his club making you fly like the dragon\n"
              "that you truly are inside.\n"
             )
        section_border()
        print(Fore.RED + "\nToo bad Dovakhiin isn't invicible,\n"
              "you flew straight to oblivion!\n")
        input(Fore.RED + "Press enter to restart ...\n" + Fore.RESET)
        section_border()
        clear()
        restart_program()


scenarioThree()


def scenarioFour():
    section_border()
    print(Fore.YELLOW + "Scenario 4: The Whimsical Werewolf")
    section_border()
    print(
          "\nYou got tired of your companion Bard singing your ears off\n"
          "so not short after your travels outside of Whiterun you\n"
          "Fos-Ro-Dah his lute into oblivion and the Bard left.\n"
          "As nightfall enters and the moon rises, you feel\n"
          "the transformation coming on. What's your approach?\n"
         )
    section_border()
    print(Fore.BLUE + "Option 1: Embrace the Dance of the Werewolf?\n"
          "Option 2: Attempt Werewolf Stand-Up Comedy?\n")

    userInput = input("Enter 1 or 2: ")

    while userInput not in {"1", "2"}:
        print("Please enter 1 or 2")
        userInput = input("Enter 1 or 2: ")
    clear()

    if userInput == "1":
        section_border()
        print(Fore.BLUE + "You entered option 1:"
              "\nEmbrace the Dance of the Werewolf!" + Fore.RESET)
        section_border()
        print(
              "\nYou transform and start a moonlit\n"
              "dance party with other werewolves.\n"
              "The locals join in, and you become the talk of the town\n"
              "as the 'Howling Dance Champion.'\n"
              "Morning comes and you decide to contune further\n"
              "along on this weird and random journey.\n"
             )
        section_border()

    elif userInput == "2":
        section_border()
        print(Fore.BLUE + "You entered option 2:"
              "\nAttempt Werewolf Stand-Up Comedy!")
        section_border()
        print(
              "\nYou try telling jokes in your werewolf form,\n"
              "but the audience finds your delivery too 'howl-arious'.\n"
              "The Jarl appoints you as the official court jester.\n"
              "You tell the Jarl thanks but no thanks, you're only\n"
              "interest right now is continuing on with your journey\n"
             )
        section_border()
    input(Fore.YELLOW + "Press enter to continue ..." + Fore.RESET)
    clear()


scenarioFour()


def scenarioFive():
    section_border()
    print(Fore.YELLOW + "Scenario 5: The Ancient Tomb of Laughter"
          + Fore.RESET)
    section_border()
    print(
          "\nYou're joined by your 'always-in-my-way' trusty companion\n"
          "Lydia and the two of you continue on your journy.\n"
          "You stumble upon an ancient tomb and start exploring it.\n"
          "Deep in the tomb you encounter a ghostly figure.\n"
          "How do you approach the situation?\n"
         )
    section_border()
    print(Fore.BLUE + "Option 1: The Ghost Whisperer?\n"
          "Option 2: Startle Stand-Up?\n")

    userInput = input("Enter 1 or 2: ")

    while userInput not in {"1", "2"}:
        print("Please enter 1 or 2")
        userInput = input("Enter 1 or 2: ")
    clear()

    if userInput == "1":
        section_border()
        print(Fore.BLUE + "You entered option 1:"
              "\nThe Ghost Whisperer!")
        section_border()
        print(
              "\nYou engage the ghost in a friendly conversation,\n"
              "discovering it's a bored bard from ancient times.\n"
              "You form a spectral band and will later tour Skyrim's crypts\n"
              "and spreading spooky merriment.\n"
              "But for now you continue back out from the crypt\n"
              "with Lydia right behind you\n"
             )
        section_border()

    elif userInput == "2":
        section_border()
        print(Fore.BLUE + "You entered option 2:"
              "\nStartle Stand-Up!")
        section_border()
        print(
              "\nYou try to tell ghost-themed jokes,\n"
              "inadvertently making the ghost laugh so hard it disappears.\n"
              "The tomb later becomes a popular comedy club for ghosts,\n"
              "and you'll gain a legion of spectral fans.\n"
              "But for now you'll continue on your journey with Lyda\n"
              "right behind you. You decide to leave the crypt to continue\n"
              "your travels\n"
             )
        section_border()
    input(Fore.YELLOW + "Press enter to continue ..." + Fore.RESET)
    clear()


scenarioFive()


def scenarioSix():
    """
    Simulates an encounter with Cicero in the crypt. Cicero presents a riddle
    that the player must solve to proceed. The function randomly selects a
    riddle from the predefined set of riddles, displays it along with
    answer options, prompts the player for input, and validates
    the response. If the answer is correct, Cicero allows the player to pass;
    otherwise, the game restarts.
    """
    """Get riddle from RIDDLES in random order"""
    riddle_index = random.randint(0, len(RIDDLES) - 1)
    selected_riddle = RIDDLES[riddle_index]

    section_border()
    print(Fore.YELLOW + "Scenario 6: Cicero the ever so annoying jester")
    section_border()
    print(
          "\nRight before leaving the crypt Cicero, \n"
          "the eccentric and annoying jester appears.\n"
          "He has sealed off the entrance and wont let you\n"
          "pass until you solve a riddle.\n"
          "'Ah Adventurer! Cicero sees you approach, yes, yes.\n"
          "But to pass, a challenge awaits, a riddle to tease \n"
          "that clever mind of yours. Oh, and a delightful one!\n"
          "Listen carefully, my dear friend':\n"
         )
    section_border()

    print(Fore.BLUE + selected_riddle["riddle"])

    for i, option in enumerate(selected_riddle["options"], start=1):
        print(f"Option {i}: {option}")

    user_input = input(f"Enter the number of your answer\
                       (1-{len(selected_riddle['options'])}): ")

    while not user_input.isdigit() or int(user_input)\
            not in range(1, len(selected_riddle['options']) + 1):
        print(f"Please enter a valid option\
              (1-{len(selected_riddle['options'])}): ")
        user_input = input(f"Enter the number of your answer\
                           (1-{len(selected_riddle['options'])}): ")

    selected_option = selected_riddle["options"][int(user_input) - 1]

    if selected_option == selected_riddle["correct_answer"]:
        clear()
        section_border()
        print(Fore.YELLOW + "\nCicero applauds your wit! You may pass.\n")
        section_border()
        print(
              "\nCongratulations! You, the dragonborn of Skyrim, managed\n"
              "to solve the riddle and continue on with your journey.\n"
              "You have turned the harsh world of Tamriel\n"
              "into a realm of laughter and joy.\n"
              "The people sing songs of your whimsical exploits,\n"
              "and you became the legendary hero of humor.\n"
              "May your journey continue to be filled with\n"
              "hilarity and merriment!\n"
             )
        section_border()
        input(Fore.YELLOW + "Press enter to restart ..." + Fore.RESET)
        clear()
        restart_program()
    else:
        clear()
        section_border()
        print(Fore.RED + "Alas! Cicero cackles with mockery.\n"
              f"The correct answer was {selected_riddle['correct_answer']}.")
        section_border()
        print("\nCicero closes the entrance and you are forced\n"
              "back down in to the crypt. You have lost the game....\n")
        section_border()
        input(Fore.RED + "Press enter to restart ..." + Fore.RESET)
        clear()
        restart_program()


scenarioSix()


    