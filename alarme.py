from datetime import datetime
from time import sleep as t
from serialLib import serialLib as s

nome, horario = input('Digite o título e horário do seu alarme, seguindo o formato nome - hh:mm:ss\n').split(' - ')
hora, minuto, segundo = horario.split(':')
hora, minuto, segundo = int(hora), int(minuto), int(segundo)
serial = s('4', 9600)

if hora < 24 and hora >= 0 and minuto < 60 and minuto >= 0 and segundo < 60 and segundo >= 0:
    while True:
        agora = str(datetime.now())
        dataAtual, horarioAtual = agora.split(' ')
        horaAtual, minutoAtual, segundoAtual = horarioAtual.split(':')
        segundoAtual = segundoAtual[0:2]
        horaAtual, minutoAtual, segundoAtual = int(horaAtual), int(minutoAtual), int(segundoAtual)

        if horaAtual == hora and minutoAtual == minuto and segundoAtual == segundo:
            while True:
                print(f'ALARME: {nome}')
                serial.send('a')
                t(1)