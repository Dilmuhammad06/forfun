# Libraries
import os

username = os.getlogin()  # Name of current user
direction = f'/home/{username}/Desktop/virus'  # Direction of the folder
num = int(input('Son kiriting: '))  # Number of files


def creator_f():  # File creator function
    cc = 0
    for c in range(1, num+1):
        cc += 1
        with open(os.path.join(direction, f'hell_{cc}.txt'), 'w') as a:
            a.write(f'File: {cc}')


try:  # Running the function
    creator_f()

except FileNotFoundError:  # If direction does not exist create it
    os.mkdir(f'/home/{username}/Desktop/virus')
    creator_f()

finally:  # The end of code
    print('Done')
