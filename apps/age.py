def main():

    import os
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
    print('For months, enter numbers 1 - 12')
    time.sleep(.3)
    birth_year = input('\nEnter your birth year, or \'n\' to exit:\n')
    if birth_year == "n":
        import main
        main.main()
    birth_month = input('Enter your birth month:\n')
    birth_day = input('Enter your birth day:\n')
    year = input('Enter the current year:\n')
    date = input('Enter the current month:\n')
    day = input('Enter the current day:\n')
    year = int(year) * 365
    birth_year = int(birth_year) * 365
    date = int(date) * 30
    birth_month = int(birth_month) * 30
    age = int(year) + int(date) + int(day)
    age2 = int(birth_year) + int(birth_month) + int(birth_day)
    age3 = int(age) - int(age2)
    age_final = int(age3) / 365
    os.system('cls')
    print('You are...')
    time.sleep(.5)
    print(age_final)
    print('years old!')
    print(' ')
    input('\n\nPress ENTER to return to the command portal.')

    import main
    main.main()
