import msvcrt
from Fonts import figFont, lines
from Authenticator import checkPassed
from ScreenCleaner import clear

def main():
    exit = False
    while not exit:
        clear()
        print(lines(80))
        print(figFont("Binary", "Slant", "red"))
        print(figFont("Authenticator", "Slant", "magenta"))
        print(lines(80))
        print('Type "Verify" to input string, "Exit" to exit')
        action = input("Action: ").lower()
        if action == "verify":
            inputting = True
            clear()
            print(lines(35))
            print(figFont("Enter the binary", "term", "yellow"))
            print(figFont("Type exit to return to home", "term", "yellow"))
            print(figFont("Type rules to show the rules", "term", "yellow"))
            print(lines(35))
            while inputting:
                binary = input().strip(" ")
                if binary.lower() == "exit":
                    inputting = False
                elif binary.lower() == "rules":
                    print(figFont("1 There must be at least 3 1's", "term", "yellow"))
                    print(figFont('2 There must be "00" in the input', "term", "yellow"))
                else:
                    print(checkPassed(binary))
                print(lines(35))
        elif action == "exit":
            exit = True
        else:
            continue
    clear()
    print(figFont("Thank you for using Binary Authenticator!", "standard", "yellow"))
    print("Click Enter to exit")

    while True:
        key = msvcrt.getch()
        if key == b'\r':
            clear()
            break

if __name__ == "__main__":
    main()