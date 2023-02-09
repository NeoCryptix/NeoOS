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

  input1 = input ('Enter text to encrypt. (all lowercase, spaces allowed)\n' + TGREEN + '>> ' + TWHITE)

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

  text = str(input1).replace("a","1").replace("b","2").replace("c","3").replace("d","4").replace("e","5").replace("f","6").replace("g","7").replace("h","8").replace("i","9").replace("j","0").replace("k","[").replace("l","]").replace("m","{").replace("n","}").replace("o","\\").replace("p","|").replace("q","/").replace("r","<").replace("s",">").replace("t","`").replace("u","^").replace("v","%").replace("w","$").replace("x","#").replace("y","@").replace("z","!")

  print ('Your encrypted text is... \n\n'+ text)

  print ('\nSince Ctrl + C is the Keyboard Interrupt shortcut, follow these steps to copy this result to clipboard. Highlight the text and right-click, then press \'Copy\'. You cannot use Ctrl + V to paste in the console, so right-click and hit \'Paste\' instead.')

  input('\n\nPress ENTER to return to the command portal.')
  import main

  main.main()