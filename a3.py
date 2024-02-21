# a3.py

# Nicole Kwan
# nkwan3@uci.edu
# 76647093

from ui import *
from menu import print_menu

# /Users/nicolekwan/Workspace/journal.dsu


def main():
    try:
        print_menu()
        while True:
            commands = ["l", "q", "c", "d", "r", "o", "e", "p"]
            user_input = input("\nEnter: ")
            command, *args = user_input.split()

            if command in commands:
                if command.lower() in ["e", "p"]:
                    run(command, args)
                else:
                    run(command, args)
            else:
                print("Invalid Command")

    except IndexError:
        print(f"Improper amount of arguments: Please enter commands in the proper format")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()