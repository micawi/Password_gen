from password import Password;
from time import sleep;
import os;

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
        sleep(1);
        generatePassword();
    if((pwlength < 6) | (pwlength > 20)):
        print("\nPassword not in bounds");
        sleep(1);
        generatePassword();    
    
    sleep(1);

    pw = Password(pwlength);
    pw.generate();
    print("\n\nPassword: " + pw.Password);
    sleep(1);

    # Save password loop
    while(True):
        toSave: str = input("\nSave Password Y/N? ");
        if(toSave == "Y"):
            try:
                print("\nEnter save location: ");
                saveLoc: str = input();
                print("\nEnter file name: ");
                fileName: str = input() + ".txt";
                cwd: str = os.getcwd();
                # change into saveLoc
                os.chdir(saveLoc);
                with open(fileName, "w") as f:
                    f.write(pw.Password);
                # change back to cwd
                os.chdir(cwd);

                sleep(1);
                print("\nPassword saved!");
                break;
            except:
                print("\nInvalid path!");
                continue;
        elif(toSave == "N"):
            break;
        else:
            print("\nInvalid answer");
            continue;


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