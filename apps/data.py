def main():

    import random,os,string
    import time

    TCYAN = '\033[36m'  # reset to the defaults
    TWHITE = '\033[37m'  # reset to the defaults
    TRED = '\033[31m'  # reset to the defaults
    TBLUE = '\033[34m'  # reset to the defaults
    TPURPLE = '\033[35m'  # reset to the defaults
    TGREEN = '\033[32m'  # reset to the defaults
    TYELLOW = '\033[33m'  # reset to the defaults
    TORANGE = '\033[33m'  # reset to the defaults
    
    from collections import Counter

    os.system('cls')

    input_string = input('Enter values in data set separated by spaces.\n' + TGREEN + '>> ' + TWHITE )


    os.system('cls')
    n_num = input_string.split(' ')

    print ('Data analysis complete.')
    print('Your data set: ' + str(n_num))
    n = len(n_num)

    get_sum = sum(float(x) for x in n_num)
    mean = get_sum / n

    print("Mean: " + str(mean))

    n = len(n_num)
    n_num.sort()

    if n % 2 == 0:
        median1 = n_num[n//2]
        median2 = n_num[(n//2) - 1]
        median = (float(median1) + float(median2)) / 2
    else:
        median = n_num[n//2]
    print("Median: " + str(median))

    n = len(n_num)

    data = Counter(n_num)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

    if len(mode) == n:
        get_mode = "Mode(s): N/A"
    else:
        get_mode = "Mode(s): " + ', '.join(map(str, mode))

    print(get_mode)

    input('\n\nPress ENTER to return to the command portal.')

    import main
    main.main()
