def main():

    import random
    import os
    import string
    import time


    TCYAN = '\033[36m'  # reset to the defaults
    TWHITE = '\033[37m'  # reset to the defaults
    TRED = '\033[31m'  # reset to the defaults
    TBLUE = '\033[34m'  # reset to the defaults
    TPURPLE = '\033[35m'  # reset to the defaults
    TGREEN = '\033[32m'  # reset to the defaults
    TYELLOW = '\033[33m'  # reset to the defaults
    TORANGE = '\033[33m'  # reset to the defaults

    os.system('cls')
    time.sleep(.5)
    print('Here is a number...')
    number1 = random.randrange(1,10000000)
    print (str(number1) + '!')

    input('\n\nPress ENTER to return to the command portal.')
    import main

    main.main()