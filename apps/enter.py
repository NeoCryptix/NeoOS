def main():

  import os

  os.system('cls')
  run = True
  press = None
  press = 0
  msg = 'Press ENTER!\n'

  while run:
    e = input(f'{msg}\nYou have pressed ENTER {press} times!\nIf you want to leave, type \'n\'. ')
    press += 1
    os.system('cls')
    if e == 'n':
      print(f'WOW! You pressed ENTER {press} times!\n')
      run = False
      input('\n\nPress ENTER to return to the command portal.')
      import main
      main.main()

    if press == 1000:
      msg = 'get a life nerd\n'

    if press == 10000:
      msg = 'go breathe air. do something else.\n'

    if press == 100000:
      msg = 'at least make sure your loved ones know you haven\'t perished.\n'

    if press == 1000000:
      msg = '(ㆆ_ㆆ) seriously\n'

