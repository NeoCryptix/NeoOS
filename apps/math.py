def main():
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
 operation = input('What operation would you like to use?\nEnter:\n+ (Addition) (addend/addend)\n- (Subtraction) ('
                   'base/sub)\n* ('
                   'Multiplication) (factor/factor)\n/ (Division) (dividend/divisor)\n** (Exponentiation) ('
                   'base/power)\n*** (Exponentiation with very large numbers, no decimals) (base/power)\n% ('
                   'Percentages) (whole/percentage)\n\n' + TGREEN + '>> ' + TWHITE )
 os.system('cls')

 if operation == '+':
  os.system('cls')
  num1 = input('First number: ')
  num2 = input('Second number: ')
  ans1 = float(num1) + float(num2)
  print('\n')
  print(str(num1) + ' plus ' + str(num2) + ' equals ' + str(ans1) + '.')

 if operation == '-':
  os.system('cls')
  num1 = input('First number: ')
  num2 = input('Second number: ')
  ans2 = float(num1) - float(num2)
  print('\n')
  print(str(num1) + ' minus ' + str(num2) + ' equals ' + str(ans2) + '.')

 if operation == '/':
  os.system('cls')
  num1 = input('First number: ')
  num2 = input('Second number: ')
  ans3 = float(num1) / float(num2)
  print('\n')
  print(str(num1) + ' divided by ' + str(num2) + ' equals ' + str(ans3) + '.')

 if operation == '*':
  os.system('cls')
  num1 = input('First number: ')
  num2 = input('Second number: ')
  ans4 = float(num1) * float(num2)
  print('\n')
  print(str(num1) + ' times ' + num2 + ' equals ' + str(ans4) + '.')

 if operation == '**':
  os.system('cls')
  num1 = input('First number: ')
  num2 = input('Second number: ')
  ans5 = pow(float(num1), float(num2))
  print('\n')
  print (str(num1) + ' to the power of ' + str(num2) + ' equals ' + str(ans5) + '.')

 if operation == '***':
  os.system('cls')
  num1 = input('First number: ')
  num2 = input('Second number: ')
  ans6 = pow(int(num1), int(num2))
  print (str(num1) + ' to the power of ' + str(num2) + ' equals ' + str(ans6 ) + '.')

 if operation == '%':
  os.system('cls')
  num1 = input('First number: ')
  num2 = input('Second number: ')
  ans7P = float(num1) / float(num2)
  ans7 = float(ans7P) * 100

  print ('\n')
  print (str(num1) + ' is ' + str(ans7) + '% of ' + str(num2) + '.')

 #if operation == 'avg':
  #os.system('cls')

  #in_num = input ('How many values are we using? ')
  #print('')

  #run = 0
  #total = 0

  #while int(in_num) > int(run):
    #inputavg = input('Enter value: ')
    #total = int(total) + int(inputavg)
    #run = run + 1

  #final = int(total) / int(in_num)
  #print ('\nThe average of those numbers is ' + str(final) + '.')
 input('\n\nPress ENTER to return to the command portal.')
 import main

 main.main()