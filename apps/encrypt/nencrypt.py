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

  input1 = input ('Enter value to encrypt. (spaces allowed)\n' + TGREEN + '>> ' + TWHITE)

  os.system('cls')

  val = input1.replace("1","-").replace("2","[").replace("3","{").replace("4","_").replace("5","/").replace("6","\\").replace("7","|").replace("8","}").replace("9","<").replace("0","]")

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

  print ('Your encrypted value is... ' + val)

  print ('Since Ctrl + C is the Keyboard Interrupt shortcut, follow these steps to copy this result to clipboard. Highlight the text and right-click, then press \'Copy\'. You cannot use Ctrl + V to paste in the console, so right-click and hit \'Paste\' instead.')
  input('\n\nPress ENTER to return to the command portal.')
  import main

  main.main()