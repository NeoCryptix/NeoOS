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

  input1 = input ('What module do you want to use?\n[1] Text Encryption\n[2] Text Decryption\n[3] Number Encryption\n['
                  '4] Number Decryption\n' + TGREEN + '>> ' + TWHITE)

  if input1 == '1':
    os.system('cls')
    import apps.encrypt.encrypt
    apps.encrypt.encrypt.main()

  if input1 == '2':
    os.system('cls')
    import apps.encrypt.decrypt
    apps.encrypt.decrypt.main()

  if input1 == '3':
    os.system('cls')
    import apps.encrypt.nencrypt
    apps.encrypt.nencrypt.main()

  if input1 == '4':
    os.system('cls')
    import apps.encrypt.ndecrypt
    apps.encrypt.ndecrypt.main()

  else:
    input('\n\nPress ENTER to return to the command portal.')
    import main
    main.main()