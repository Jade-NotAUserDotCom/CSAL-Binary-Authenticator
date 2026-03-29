import sys, msvcrt
from Fonts import figFont, lines
from Authenticator import checkPassed
from ScreenCleaner import clear

def main():
    exit = False
    while not exit:
        clear()
        print(lines())
        print(figFont("Binary Authenticator", "Slant", "red"))
        print(lines())
        print('Type "Verify" to input string, "Exit" to exit')
        action = input("Action: ").lower()
        if action == "verify":
            inputting = True
            clear()
            print(lines())
            print(figFont("Enter the binary", "digital", "cyan"))
            print(figFont("Type exit to return to home", "digital", "cyan"))
            print(figFont("Type rules to show the rules of a valid binary", "digital", "cyan"))
            print(lines())
            while inputting:
                binary = input()
                if binary.lower() == "exit":
                    inputting = False
                elif binary.lower() == "rules":
                    print(figFont("1. There must be at lease 3 1's", "digital", "magenta"))
                    print(figFont('2. There must be "00" in the input', "digital", "magenta"))
                else:
                    print(checkPassed(binary))
                print(lines())
        elif action == "exit":
            exit = True
        else:
            continue
    clear()
    print(figFont("Thank You for using Binary Authenticator!", "shadow", "yellow"))
    print("Click Enter to exit")

    while True:
        key = msvcrt.getch()
        if key == b'\r':
            clear()
            break

if __name__ == "__main__":
    main()