# Libraries
import os
import datetime

# Variables
date = datetime.datetime.now()
year = date.year
month = date.month
day = date.day
direction = '/media/dilmuhammad/8404455904454F7C/Auto Delete/Keep In Secret'
files = []

# Listing files from that direction
for i in os.listdir(direction):
    if i != 'deleter_script.py' and i != 'log.txt':
        files.append(i)

# If code runs correctly
try:
    # Deleted files counter
    counter = 0

    # Deleting files
    for i in files:
        counter = +1
        os.remove(f'/media/dilmuhammad/8404455904454F7C/Auto Delete/Keep In Secret/{i}')

        # Writing a log file
        with open('log.txt', 'a+') as a:
            a.write(f'File name: {i}, date: {year, month, day} \n')
            a.seek(0)

    print(f'{counter} amount of files have been deleted')

# If code has FileNotFoundError error
except FileNotFoundError:
    print('Not found 404')

    # Writing a log file
    with open('log.txt', 'a+') as a:
        a.write(f'File not found, date: {year, month, day} \n')
        a.seek(0)

# The end of the code
finally:
    print('Script successfully has been stopped')
