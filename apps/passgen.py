def main():
    
    import os
    import random
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
    
    print('Welcome to PassGen Mini 1.1 (NeoOS) by the NeoCryptix Python Team!')
    
    adjective = [
    'time.sleepy', 'fat', 'fluffy', 'white', 'proud', 'brave', 'fast', 'boopable',
        'funny', 'stinky', 'holy', 'gentle', 'gigantic', 'busy', 'jumbled',
        'foolish', 'Crazy', 'giant', 'bookish', 'mini', 'red', 'orange', 'yellow',
        'green', 'blue', 'Purple', 'Indigo', 'violent', 'jumpy', 'Stretchy',
        'glittery', 'clear', 'transparent', 'Rubbery', 'idiotic', 'sticky',
        'tough', 'weak', 'salty', 'sweet', 'sour', 'bitter', 'spotted', 'striped',
        'underscored', 'hashtagged', 'Flexible', 'spiraling', 'Huge', 'tiny',
        'Miniscule', 'furry', 'powerful', 'Hot', 'Cold', 'Timid', 'spongey',
         'dead','Immpressive','Spiky','Dry','Soft','Encrypted','Dusty','Solid','Gooey','Turquoise','Expected','Round','Situated','InPain','Tired','time.sleepy','Black','SeaBlue',''
    ]
    
    noun = [
    'truck', 'PS5', 'apple', 'pencil', 'pen', 'eraser', 'rabbit', 'book',
        'plant', 'tree', 'tin', 'hashtag', 'robot', 'mouse', 'plate', 'computer',
        'microphone', 'printer', 'website', 'marker', 'crayon', 'wheel', 'truck',
        'toaster', 'goat', 'dinosaur', 'Bennet', 'ball', 'dragon', 'hammer', 'duck', 'panda',
        'pig', 'hydra', 'crab', 'pikachu', 'steve', 'alex', 'king', 'slime',
        'person', 'family', 'bamboo', 'broom', 'desk', 'doll', 'flower', 'mango',
        'potato', 'radio', 'witch', 'horse', 'candy', 'loaf', 'idiot', 'Cat',
        'Dog', 'coat', 'chair', 'Star', 'Human', 'bed', 'Frog', 'Owl','RollerCoaster','Blanket','Rock','Coat','Ear','Collar','Body','Painting','RubixCube','Spaceship','Firetruck','Sphere','Cube','Lego','Horse','Duck','Sheep','Cow','Goat','Pig','GuineaPig','Llama','Camel','Bee','Bear','Butterfly','Beetle','Coyote','Raccoon','Hedgehog','Otter','OakTree','Eagle','Parrot','Monkey','BoaConstrictor','Anaconda','Crocodile','Jaguar','Anteater','KingCobra','Macaw','Coconut','Lion','Hyena','Toad','Rhinoceros','Buffalo','Vulture','Elephant','Hippopotamus','Kangaroo','Deer','Gazelle','Cactus'
    ]
    
    start = ['the', 'a', '_']
    
    adjective = random.choice(adjective)
    noun = random.choice(noun)
    number = random.randrange(1, 1000)
    special_char = random.choice(string.punctuation)
    special_char2 = random.choice(string.punctuation)
    start = random.choice(start)
    num_ex = str(number)
    
    char = input('Do you want your password to include special characters? y/n\n' + TGREEN + '>> ' + TWHITE )
    
    if char == 'y':
        generated_password = start + adjective + noun + num_ex + special_char + special_char2
    
    if char == 'n':
        generated_password = start + adjective + noun + num_ex
    
    os.system('cls')
    
    time.sleep(.5)
    print('\n-Generating... ')
    time.sleep(.2)
    print('-Confirming... ')
    time.sleep(.2)
    print('-Finalizing...')
    time.sleep(.2)
    print('-Printing... \n')
    time.sleep(.2)
    print('[ ' + generated_password + ' ]')
    
    print('\nThank you for using PassGen Mini!')
    restart = input('\n\nPress ENTER to return to the command portal, or \'1\' to generate a new password. ')
    
    if restart == "1":
        exec(open("apps/passgen.py").read())
    
    import main
main.main()
