def easy():
  
  import random
  import os
  import string
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
  
  name = input ('What is your cat\'s name? ')
  breed = input ('What breed is ' + name + '? ')
  maleorfemale = input ('Is ' + name + ' male or female (m/f)? ')
  
  if maleorfemale == 'm':
    actpron = 'he'
    refpron = 'him'
    pospron = 'his'
    cactpron = 'He'
    cpospron = 'His'
  
  if maleorfemale == 'f':
    actpron = 'she'
    refpron = 'her'
    pospron = 'hers'
    cactpron = 'She'
    cpospron = 'Her'
  
  else:
    actpron = 'unknown'
    refpron = 'unknown'
    pospron = 'unknown'
    cactpron = 'unknown'
    cpospron = 'unknown'
  
  alive = True
  
  hunger = 0
  thirst = 0
  sadness = 0
  tiredness = 0
  
  love = 0
  
  vet = 0
  
  while alive:
    os.system('cls')
   
    print ('Hunger: ' + str(hunger))
    print ('Thirst: ' + str(thirst))
    print ('Sadness: ' + str(sadness))
    print ('Tiredness: ' + str(tiredness))
    print ('Make sure none of those numbers reach 10!')
  
    cont = input ('Press ENTER to continue. ')
  
    os.system('cls')
   
    menu = input ('1) Feed ' + name + '\n2) Give ' + name + ' a drink\n3) Play with ' + name + '\n4) Pet ' + name +
                  '\n5) Let ' + name + ' have a nap\n6) Take ' + name + ' to the vet\nENTER) Do nothing\n' + TGREEN + '>> ' + TWHITE )
  
    os.system('cls')
  
    if menu == '1':
     if hunger > 1:
        hunger = hunger - 1
     else:
        print (name + ' isn\'t hungry.')
  
    if menu == '2':
     if thirst > 1:
        thirst = thirst - 1
     else:
        print (name + ' isn\'t thirsty.')
  
    if menu == '3':
     if sadness > 1:
        sadness = sadness - 1
     tiredness = tiredness + 1
     hunger = hunger + 0.5
     thirst = thirst + 0.5
  
    if menu == '4':
      if sadness > 1:
        sadness = sadness - 1
  
    if menu == '5':
      if tiredness > 1:
        tiredness = tiredness - 1
      else:
        print (name + ' isn\'t tired.')
  
    if menu == '6':
      if vet == 2:
        print('You try to put ' + name + ' back in the carrier, but ' + actpron + ' lunges at you, hissing, with claws extended. You see red, then black.\n\nYou Died.')
        input('\n\nPress ENTER to return to the command portal.')
        alive = False
        love = None
        hunger = None
        thirst = None
        tiredness = None
        sadness = None
        import main
        main.main()
        
      if vet == 1:
        hunger = 0
        thirst = 0
        sadness = 3
        tiredness = 0
        print(name + ' is refreshed, but jeez! You\'ve taken ' + refpron + ' to the vet twice! ' + cactpron + '\'s angry!')
        vet = vet + 1
      if vet == 0:
        hunger = 0
        thirst = 0
        sadness = 2
        tiredness = 0
        print (name + ' feels better, but ' + actpron + '\'s a bit annoyed.')
        vet = vet + 1
  
    cont2 = input ('Press ENTER to continue. ')
  
    hunger = hunger + .5
    thirst = thirst + .5
    tiredness = tiredness + .5
    sadness = sadness + .5
  
    love = love + 1
  
    os.system('cls')
  
    if love >= 50:
      os.system('cls')
      print('Whoa! ' + name + ' pulled a Clifford and grew to the size of a house from your love! ' + cactpron + '\'s immortal now!')
      input('\n\nPress ENTER to return to the command portal.')
      alive = False
      love = None
      hunger = None
      thirst = None
      tiredness = None
      sadness = None
      import main
      main.main()
  
    if hunger >= 10:
      death = 'starvation'
      os.system('cls')
      print ('Oh no! ' + name + ' the ' + breed + ' cat died of ' + death + '. R.I.P.')
      input('\n\nPress ENTER to return to the command portal.')
      alive = False
      love = None
      hunger = None
      thirst = None
      tiredness = None
      sadness = None
      import main
      main.main()
    
    if sadness >= 10:
      death = 'a broken heart'
      os.system('cls')
      print ('Oh no! ' + name + ' the ' + breed + ' cat died of ' + death + '. R.I.P.')
      input('\n\nPress ENTER to return to the command portal.')
      alive = False
      love = None
      hunger = None
      thirst = None
      tiredness = None
      sadness = None
      import main
      main.main()
    
    if thirst >= 10:
      death = 'dehydration'
      os.system('cls')
      print ('Oh no! ' + name + ' the ' + breed + ' cat died of ' + death + '. R.I.P.')
      input('\n\nPress ENTER to return to the command portal.')
      alive = False
      love = None
      hunger = None
      thirst = None
      tiredness = None
      sadness = None
      import main
      main.main()
    
    if tiredness >= 10:
      death = 'exhaustion'
      os.system('cls')
      print ('Oh no! ' + name + ' the ' + breed + ' cat died of ' + death + '. R.I.P.')
      input('\n\nPress ENTER to return to the command portal.')
      alive = False
      love = None
      hunger = None
      thirst = None
      tiredness = None
      sadness = None
      import main
      main.main()


def hard():
  import random
  import os
  import string
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

  name = input('What is your cat\'s name? ')
  breed = input('What breed is ' + name + '? ')
  maleorfemale = input('Is ' + name + ' male or female (m/f)? ')

  alive = True

  hunger = 0
  thirst = 0
  sadness = 0
  tiredness = 0

  love = 0

  if maleorfemale == 'm':
    actpron = 'he'
    refpron = 'him'
    pospron = 'his'
    cactpron = 'He'
    cpospron = 'His'

  if maleorfemale == 'f':
    actpron = 'she'
    refpron = 'her'
    pospron = 'hers'
    cactpron = 'She'
    cpospron = 'Her'

  else:
    actpron = 'unknown'
    refpron = 'unknown'
    pospron = 'unknown'
    cactpron = 'unknown'
    cpospron = 'unknown'

  while alive:
    os.system('cls')

    print('Hunger: ' + str(hunger))
    print('Thirst: ' + str(thirst))
    print('Sadness: ' + str(sadness))
    print('Tiredness: ' + str(tiredness))
    print('Make sure none of those numbers reach 10!')

    cont = input('Press ENTER to continue. ')

    os.system('cls')

    menu = input(
      '1) Feed ' + name + '\n2) Give ' + name + ' a drink\n3) Play with ' + name + '\n4) Pet ' + name + '\n5) Let ' +
      name + ' have a nap\nENTER) Do nothing\n' + TGREEN + '>> ' + TWHITE )

    os.system('cls')

    if menu == '1':
      if hunger > 1:
        hunger = hunger - .5
      else:
        print(name + ' isn\'t hungry.')

    if menu == '2':
      if thirst > 1:
        thirst = thirst - .5
      else:
        print(name + ' isn\'t thirsty.')

    if menu == '3':
      if sadness > 1:
        sadness = sadness - .5
      tiredness = tiredness + 1
      hunger = hunger + 0.5
      thirst = thirst + 0.5

    if menu == '4':
      if sadness > 1:
        sadness = sadness - .5

    if menu == '5':
      if tiredness > 1:
        tiredness = tiredness - .5
      else:
        print(name + ' isn\'t tired.')

    cont2 = input('Press ENTER to continue. ')

    plus = random.uniform(.1, 2)
    hunger = hunger + plus
    plus = random.uniform(.1, 2)
    thirst = thirst + plus
    plus = random.uniform(.1, 2)
    tiredness = tiredness + plus
    plus = random.uniform(.1, 2)
    sadness = sadness + plus

    love = love + 1

    if love >= 75:
      print(
        'Whoa! ' + name + ' pulled a Clifford and grew to the size of a house from your love! ' + cactpron + '\'s immortal now!')
      input('\n\nPress ENTER to return to the command portal.')
      alive = False
      love = None
      hunger = None
      thirst = None
      tiredness = None
      sadness = None
      import main
      main.main()

    if hunger >= 10:
      death = 'starvation'
      print('Oh no! ' + name + ' the ' + breed + ' cat died of ' + death + '. R.I.P.')
      input('\n\nPress ENTER to return to the command portal.')
      alive = False
      love = None
      hunger = None
      thirst = None
      tiredness = None
      sadness = None
      import main
      main.main()

    if sadness >= 10:
      death = 'a broken heart'
      print('Oh no! ' + name + ' the ' + breed + ' cat died of ' + death + '. R.I.P.')
      input('\n\nPress ENTER to return to the command portal.')
      alive = False
      love = None
      hunger = None
      thirst = None
      tiredness = None
      sadness = None
      import main
      main.main()

    if thirst >= 10:
      death = 'dehydration'
      print('Oh no! ' + name + ' the ' + breed + ' cat died of ' + death + '. R.I.P.')
      input('\n\nPress ENTER to return to the command portal.')
      alive = False
      love = None
      hunger = None
      thirst = None
      tiredness = None
      sadness = None
      import main
      main.main()

    if tiredness >= 10:
      death = 'exhaustion'
      print('Oh no! ' + name + ' the ' + breed + ' cat died of ' + death + '. R.I.P.')
      input('\n\nPress ENTER to return to the command portal.')
      alive = False
      love = None
      hunger = None
      thirst = None
      tiredness = None
      sadness = None
      import main
      main.main()
  
