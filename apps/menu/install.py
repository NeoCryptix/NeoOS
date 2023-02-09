def main():

    import os, time


    os.system('cls')

    print ('Example:\nCommand: web\nDirectory: apps.webpage\nFunction: main()')

    TCYAN = '\033[36m'  # reset to the defaults
    TWHITE = '\033[37m'  # reset to the defaults
    TRED = '\033[31m'  # reset to the defaults
    TBLUE = '\033[34m'  # reset to the defaults
    TPURPLE = '\033[35m'  # reset to the defaults
    TGREEN = '\033[32m'  # reset to the defaults
    TYELLOW = '\033[33m'  # reset to the defaults
    TORANGE = '\033[33m'  # reset to the defaults

    cmd = input('\nEnter the command that will activate your app, or nothing to exit.\n' + TGREEN + '>> ' + TWHITE)

    if cmd == '':
        import main
        main.main()

    drc = input('Where is your app located? apps.[filename, no extension]\n' + TGREEN + '>> ' + TWHITE)
    fn = input('What function will this command run in your selected file? [function name]()')
    os.system('cls')

    install = open('main.py', 'a')
    command = [f'\n\nif osmenu == \'{cmd}\':\n    os.system(\'cls\')\n    import {drc}\n    {drc}.{fn}',]
    install.writelines(command)
    install.close()

    print('Your app has been installed.')

    time.sleep(2)

    os.system('cls')



    input('\n\nPress ENTER to return to the command portal.')
    import main

    main.main()