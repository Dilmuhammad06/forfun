import datetime
import time


houro = int(input('Soatni kiriting: '))
mino = int(input('Minutni kiriting: '))

def Clock():
    current = datetime.datetime.now().hour, datetime.datetime.now().minute
    hour = current[0]
    minute = current[1]
    if hour == houro and minute == mino:
        print('Happy New Year')
    else:
        print('not yet')
        print(f'Current: {hour}:{minute}')
        print(f'{houro-hour}:{mino-minute} left')

while True:
    a = True
    while a:
        Clock()
        time.sleep(15)
        a = False