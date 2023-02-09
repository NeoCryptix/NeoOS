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

    while True:
        os.system('cls')
        osmenu = None
        osmenu = input(TWHITE + 'Enter command\n' + TGREEN + '>> ' + TWHITE)

        if osmenu == 'os':
            os.system('cls')
            import apps.os
            apps.os.main()

        if osmenu == 'age':
            os.system('cls')
            import apps.age
            apps.age.main()

        if osmenu == 'convert':
            os.system('cls')
            import apps.convert
            apps.convert.main()

        if osmenu == 'data':
            os.system('cls')
            import apps.data
            apps.data.main()

        if osmenu == 'encrypt':
            os.system('cls')
            import apps.encryptmain
            apps.encryptmain.main()

        if osmenu == 'enter':
            os.system('cls')
            import apps.enter
            apps.enter.main()

        if osmenu == 'calc':
            os.system('cls')
            import apps.math
            apps.math.main()

        if osmenu == 'number':
            os.system('cls')
            import apps.number
            apps.number.main()

        if osmenu == 'rps':
            os.system('cls')
            import apps.rps
            apps.rps.main()

        if osmenu == 'counter':
            os.system('cls')
            import apps.tkcounter.counter
            apps.tkcounter.counter.main()

        if osmenu == 'neotext':
            os.system('cls')
            import apps.neotext
            apps.neotext.main()

        if osmenu == 'passgen':
            os.system('cls')
            import apps.passgen
            apps.passgen.main()

        if osmenu == 'cat':
            import apps.cat.cat
            os.system('cls')
            diff = input ("Enter hard mode? y/n ' + TGREEN + '>> ' + TWHITE ")
            if diff == 'y':
                apps.cat.cat.hard()
            apps.cat.cat.easy()

        if osmenu == 'animate':
            os.system('cls')
            import apps.animate
            apps.animate.main()

main()