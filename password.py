from random import randint;


class Password():
    # Properties
    Password: str;
    Chars: int;

    # Init
    def __init__(self, chars: int):
        self.Chars = chars;
        self.Password = "";

    # Generation
    def generate(self):
        lowerCase: str = "abcdefghijklmnopqrstuvwxyz";
        upperCase: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        specChar: str = "#+!$%&§";
        num: str = "0123456789";
        char: str;
        hasLowerCase: bool = False;
        hasUpperCase: bool = False;
        hasSpecChar: bool = False;
        hasNum: bool = False;

        for i in range(0, self.Chars):
            selCase: int = randint(0, 3);
            if(selCase == 0):
                charnum: int = randint(0, len(lowerCase) - 1);
                char = lowerCase[charnum];
                hasLowerCase = True;
            elif(selCase == 1):
                charnum: int = randint(0, len(upperCase) - 1);
                char = upperCase[charnum];
                hasUpperCase = True;
            elif(selCase == 2):
                charnum: int = randint(0, len(specChar) - 1);
                char = specChar[charnum];
                hasSpecChar = True;
            elif(selCase == 3):
                charnum: int = randint(0, len(num) - 1);
                char = num[charnum];
                hasNum = True;
            self.Password += char;
        
        if((hasLowerCase) & (hasUpperCase)
        & (hasSpecChar) & (hasNum)):
            return;
        else:
            self.Password = "";
            self.generate();