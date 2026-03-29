#The authenticator Library

import re 

def checkPassed(binary):

    # color constants
    colors = {
        "red": '\033[31m',
        "green": '\033[32m',
        "reset": '\033[0m'
    }

    # check if input only comtains 0 and 1
    if re.fullmatch(f"[01]+", binary):
    
        # condition: at least 3 "1" and two consecutive 0's
        if binary.count("1") >= 3 and "00" in binary:
            return f"{colors['green']}Your input is Accepted.{colors['reset']}"
    
        # condition does not meet
        else:
            return f"{colors["red"]}Your input is Not Accepted.{colors["reset"]}"
    
    # result if string contains other char than 1 and 0
    else:
        return f"{colors["red"]}Your input is not a binary. (Contain only 1 and 0){colors['reset']}"
    
