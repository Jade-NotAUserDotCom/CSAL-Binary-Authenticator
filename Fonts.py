from pyfiglet import Figlet

def figFont(text, font, color):
    colors = {
        "red": '\033[31m',
        "green": '\033[32m',
        "yellow": '\033[33m',
        "magenta": '\033[35m',
        "cyan": '\033[36m',
        "reset": '\033[0m'
    }

    word = Figlet(font = font).renderText(text)

    return colors[color] + word + colors['reset']

def lines():

    word = ""

    for _ in range(80):
        word += "="
    
    return word