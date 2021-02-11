import pyautogui as auto
import time as t

msgs = ['!w',
        '!t',
        '!overtime',
        '!buy music',
        '!buy karaoke',
        '!buy chef',
        '!buy flipper',
        '!buy airplane',
        '!clean',
        '!daily',
        '!b',
        '!g',
        '!vote']

while True:
    run = input('Deseja iniciar? ')

    if run == 'sim':
        t.sleep(4)

        for i in msgs:
            auto.typewrite(i)
            auto.press("enter")
            t.sleep(1)
        break
    
    else:
        print('Resposta não reconhecida. Tente novamente.\n')

