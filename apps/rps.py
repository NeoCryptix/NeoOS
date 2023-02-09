def main():
    import os
    import string
    import random
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
    RPS_List = ['rock','paper','scissors']

    while True:
     os.system('cls')
     print ('I\'m ready!')
     time.sleep(.5)
     RPSChoice = input('\nWhat is your choice?\n(rock/paper/scissors) ' + TGREEN + '>> ' + TWHITE )

     if RPSChoice not in RPS_List:
        print("That is not an option!")
        import apps.rps
        apps.rps.main()

     COM_RPS_Choice = random.choice(RPS_List)
     print('\nMy choice is ' + COM_RPS_Choice + '!')

     if RPSChoice == 'rock':
       if COM_RPS_Choice == 'rock':
         print('Tie! :)')

       if COM_RPS_Choice == 'scissors':
         print ('You win!')

       if COM_RPS_Choice == 'paper':
         print ('You lose...')


     if RPSChoice == 'scissors':
       if COM_RPS_Choice == 'scissors':
         print('Tie! :)')

       if COM_RPS_Choice == 'paper':
         print ('You win!')

       if COM_RPS_Choice == 'rock':
         print ('You lose...')


     if RPSChoice == 'paper':
       if COM_RPS_Choice == 'paper':
         print('Tie! :)')

       if COM_RPS_Choice == 'rock':
         print ('You win!')

       if COM_RPS_Choice == 'scissors':
         print ('You lose...')

     inputrps = input ('\nPlay again? ENTER for yes, \'n\' for no: ')

     if inputrps == 'n':
         input('\n\nPress ENTER to return to the command portal.')
         import main
         main.main()