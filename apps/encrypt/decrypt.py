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

  input1 = input ('Enter text to decrypt. (all lowercase, spaces allowed)\n' + TGREEN + '>> ' + TWHITE )

  os.system('cls')

  def load():
    print('- Loading')
    time.sleep(.2)
    os.system('cls')

    print('\ Loading')
    time.sleep(.2)
    os.system('cls')

    print('| Loading')
    time.sleep(.2)
    os.system('cls')

    print('/ Loading')
    time.sleep(.2)
    os.system('cls')

    print('- Loading')
    time.sleep(.2)
    os.system('cls')

    print('\ Loading')
    time.sleep(.2)
    os.system('cls')

    print('| Loading')
    time.sleep(.2)
    os.system('cls')

    print('/ Loading')
    time.sleep(.2)
    os.system('cls')

  load()

  text = str(input1).replace("1","a").replace("2","b").replace("3","c").replace("4","d").replace("5","e").replace("6","f").replace("7","g").replace("8","h").replace("9","i").replace("0","j").replace("[","k").replace("]","l").replace("{","m").replace("}","n").replace("\\","o").replace("|","p").replace("/","q").replace("<","r").replace(">","s").replace("`","t").replace("^","u").replace("%","v").replace("$","w").replace("#","x").replace("@","y").replace("!","z")

  print ('Your decrypted text is... '+ text)

  print ('Since Ctrl + C is the Keyboard Interrupt shortcut, follow these steps to copy this result to clipboard. Highlight the text and right-click, then press \'Copy\'. You cannot use Ctrl + V to paste in the console, so right-click and hit \'Paste\' instead.')
  input('\n\nPress ENTER to return to the command portal.')
  import main
  main.main()