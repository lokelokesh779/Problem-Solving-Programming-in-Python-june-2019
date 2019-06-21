import re

def phoneNumberValidator(number):
    pattern='^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$/[+][9][1][6-9][0-9]{9}'
    if re.match(pattern,str(number)):
        print("valid NUmber")
    else:
        print("Invalid Number")
        
        
        
import re

def emailValidator(email):
    pattern='[0-9a-z][0-9a-z]{4,13}[0-9a-z][@][0-9a-z]{3,17}[.][a-z]{2,4}$'
    if re.match(pattern,email):
        return True
    return False