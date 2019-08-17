# -- START IMPORTS --
import time
import random


# -- GLOBAL VARIABLES--
enemy_list = ['Cyclops', 'Dragon', 'Titan', 'Troll']
enemy = random.choice(enemy_list)
weapon = []


# -- FUNCTIONS --
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        choice = input(prompt).lower()
        if option1 in choice:
            break
        elif option2 in choice:
            break
        else:
            print_pause("(please enter a valid input)")
    return choice


def play_again():
    choice = valid_input("\nWould you like to play again?\n"
                         "(Please enter y or n.)\n",
                         "y", "n")
    if "y" in choice:
        print_pause("\nExcellent! Restarting the game...")
        start_game()
    elif "n" in choice:
        print_pause("\nSee you next time!")


def intro():
    print_pause("\nYou find yourself standing in the open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somwhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.")


def field():
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    choice = valid_input("\nWhat would you like to do?\n"
                         "(Please enter 1 or 2.)\n",
                         "1", "2")
    if "1" in choice:
        house()
    elif "2" in choice:
        cave()


def house():
    print_pause("\nYou approach the door of the house.")
    print_pause("You are about to knock the door... when the door "
                f"opens and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    if "sword" not in weapon:
        print("You feel a bit under-prepared for this, what with only "
              "having a tiny dagger.\n")
    print_pause(f"Enter 1 to Fight the {enemy}.")
    print_pause("Enter 2 to RUN AWAY!")
    choice = valid_input("\nWhat would you like to do?\n"
                         "(Please enter 1 or 2.)\n",
                         "1", "2")
    if "1" in choice:
        if "sword" in weapon:
            print_pause(f"\nAs the {enemy} moves to attack, you unseath "
                        "your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in "
                        "your hand as you brace yourself for the attack.")
            print_pause(f"But the {enemy} takes one look at your "
                        "shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {enemy}.")
            print_pause("You are victorious!")
            play_again()
        else:
            print_pause("\nYou do your best...")
            print_pause(f"but your dagger is no match for the {enemy}")
            print_pause("You have been defeated!")
            play_again()
    elif "2" in choice:
        print_pause("You head back to the field.")
        field()


def cave():
    print_pause("\nYou peer cautiously into the cave.")
    if "sword" in weapon:
        print_pause("You've been here before and took all the good stuff.")
        print_pause("It is just an empty cave now.")
    else:
        print_pause("\nIt turns out to be only a very small cave.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the "
                    "sword with you.")
        weapon.append("sword")
    print_pause("\nYou walk back out to the field.")
    field()


# -- module --
def start_game():
    intro()
    field()


# -- START --
start_game()
