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

        for i in range(0, self.Chars):
            selCase: int = randint(0, 3);
            if(selCase == 0):
                charnum: int = randint(0, len(lowerCase) - 1);
                char = lowerCase[charnum];
            elif(selCase == 1):
                charnum: int = randint(0, len(upperCase) - 1);
                char = upperCase[charnum];
            elif(selCase == 2):
                charnum: int = randint(0, len(specChar) - 1);
                char = specChar[charnum];
            elif(selCase == 3):
                charnum: int = randint(0, len(num) - 1);
                char = num[charnum];
            self.Password += char;