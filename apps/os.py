def main():

 TCYAN = '\033[36m'  # reset to the defaults
 TWHITE = '\033[37m'  # reset to the defaults
 TRED = '\033[31m'  # reset to the defaults
 TBLUE = '\033[34m'  # reset to the defaults
 TPURPLE = '\033[35m'  # reset to the defaults
 TGREEN = '\033[32m'  # reset to the defaults
 TYELLOW = '\033[33m'  # reset to the defaults
 TORANGE = '\033[33m'  # reset to the defaults

 menu = input(TWHITE + "[info] View OS info\n[github] View GitHub page\n[exit] Exit\n" + TGREEN + '>> ' + TWHITE)

 if menu == 'info':
    import apps.menu.info
    apps.menu.info.main()

 if menu == 'github':
    import webbrowser
    url = "https://github.com/NeoCryptix/NeoOS"
    webbrowser.open(url, new=0, autoraise=True)

 if menu == 'exit':
    import main
    main.main()