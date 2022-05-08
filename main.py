from password import Password;
from time import sleep;

# Application version
appVersion: str = "v1.0";

# Check app start
isStart: bool = True;

# Get desired length and generate password
def generatePassword():
    print("\n\nDesired password length: ");
    pwlength: str = input();
    try:
        pwlength = int(pwlength);
    except:
        print("\nInvalid password length");    

# Main program loop
while(True):
    if(isStart):
        print("\n\nWelcome to Password gen " + appVersion);
        sleep(1);
        isStart = False;
    
    print("\n\n1. Generate password");
    print("\n2. Exit program");
    selection: str = input("\n");
    if(selection == "1"):
        sleep(1);
        generatePassword();
    elif(selection == "2"):
        print("\n\nGoodbye!");
        sleep(1);
        break;