def main():

 import os
 import string
 import time
 
 time.sleep(.5)

 TCYAN = '\033[36m'  # reset to the defaults
 TWHITE = '\033[37m'  # reset to the defaults
 TRED = '\033[31m'  # reset to the defaults
 TBLUE = '\033[34m'  # reset to the defaults
 TPURPLE = '\033[35m'  # reset to the defaults
 TGREEN = '\033[32m'  # reset to the defaults
 TYELLOW = '\033[33m'  # reset to the defaults
 TORANGE = '\033[33m'  # reset to the defaults

 os.system('cls')
 print ('1) Kilograms > Pounds\n2) Pounds > Kilograms\n3) Kilometers > Miles\n4) Miles > Kilometers\n5) Celsius > '
        'Fahrenheit\n6) Fahrenheit > Celsius\n7) Meters > Yards\n8) Yards > Meters\n9) Liters > Gallons\n10) Gallons > '
        'Liters')

 input1 = input ('\nEnter the number that corresponds to which units\nyou want to convert, or press ENTER to '
                 'exit!!\n' + TGREEN + '>> ' +
                 TWHITE)

 if input1 == '1':
  os.system('cls')
  input2 = input ('Enter the amount of kg you want to convert to lbs!\n' + TGREEN + '>> ' + TWHITE)
  lbs1 = float(input2) * 2.2046
  print (TWHITE + 'That is the same as...')
  time.sleep(.5)
  print (lbs1)
  print('pounds!')
  time.sleep(.1)

 if input1 == '2':
  os.system('cls')
  input3 = input ('Enter the amount of lbs you want to convert to kg!\n' + TGREEN + '>> ' + TWHITE)
  kg1 = float(input3) / 2.205
  print (TWHITE + 'That is the same as...')
  time.sleep(.5)
  print (kg1)
  print('kilograms!')
  time.sleep(.1)

 if input1 == '3':
  os.system('cls')
  input4 = input ('Enter the amount of km you want to convert to miles! \n' + TGREEN + '>> ' + TWHITE)
  km1 = float(input4) / 1.609344
  print (TWHITE + 'That is the same as...')
  time.sleep(.5)
  print (km1)
  print('miles!')
  time.sleep(.1)

 if input1 =='4':
  os.system('cls')
  input5 = input ('Enter the amount of miles you want to convert to km! \n' + TGREEN + '>> ' + TWHITE)
  miles1 = float(input5) * 1.609344
  print (TWHITE + 'That is the same as...')
  time.sleep(.5)
  print (miles1)
  print('kilometers!')
  time.sleep(.1)

 if input1 == '5':
  os.system('cls')
  input6 = input('Enter the amount of degrees in Celsius you want to convert to  degrees in Fahrenheit! \n' + TGREEN + '>> ' + TWHITE)
  cels1 = float(input6) * 1.8
  cels2 = float(cels1) + 32
  print (TWHITE + 'That is the same as...')
  time.sleep(.5)
  print (cels2)
  print('degrees Celsius!')
  time.sleep(.1)

 if input1 == '6':
  os.system('cls')
  input7 = input('Enter the amount of degrees in Fahrenheit you want to convert to  degrees in Celsius! \n' + TGREEN + '>> ' + TWHITE)
  fahr1 = float(input7) - 32
  fahr2 = float(fahr1) * .5556
  print (TWHITE + 'That is the same as...')
  time.sleep(.5)
  print (fahr2)
  print('degrees Celcius!')
  time.sleep(.1)

 if input1 == '7':
  os.system('cls')
  input8 = input('Enter the amount of meters you want to convert to yards!\n' + TGREEN + '>> ' + TWHITE)
  mtr1 = float(input8) * 1.093613
  print (TWHITE + 'That is the same as...')
  time.sleep(.5)
  print (mtr1)
  print('yards!')
  time.sleep(.1)

 if input1 == '8':
  os.system('cls')
  input9 = input('Enter the amount of yards you want to convert to meters!\n' + TGREEN + '>> ' + TWHITE)
  yrd1 = float(input9)  * 0.9144
  print(TWHITE + 'That is the same as...')
  time.sleep(.5)
  print (yrd1)
  print('meters!')
  time.sleep(.1)

 if input1 == '9':
  os.system('cls')
  input10 = input('Enter the amount of liters you want to convert to gallons!\n' + TGREEN + '>> ' + TWHITE)
  ltr1 = float(input10)  * 0.264172
  print(TWHITE + 'That is the same as...')
  time.sleep(.5)
  print (ltr1)
  print('gallons!')
  time.sleep(.1)

 if input1 == '10':
  os.system('cls')
  input11 = input('Enter the amount of gallons you want to convert to liters!\n' + TGREEN + '>> ' + TWHITE)
  gal1 = float(input11) * 3.785412
  print(TWHITE + 'That is the same as...')
  time.sleep(.5)
  print (gal1)
  print('liters!')
  time.sleep(.1)

 input('\n\nPress ENTER to return to the command portal.')

 import main
 main.main()