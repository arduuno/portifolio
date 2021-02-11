import pyautogui, time

def perguntas():
    num = int(input('Quantas mensagens você deseja enviar? (Máx. recomendado: 1000) '))
    print('')
    txt = input('Qual mensagem deseja enviar? (Obs.: Não utilize caracteres especiais ou acentos) ')
    print('')

    print('Número de mensagens: {}'.format(num))
    print('Mensagem escolhida: {}'.format(txt))
    print('')
    ask = input('Deseja iniciar? (sim/não) ')

    if ask == 'sim':
        
        for a in range (4):
            print('.')
            time.sleep(1)

        pyautogui.typewrite('Hora do SPAM, serao enviadas {} mensagens'.format(num))
        pyautogui.press("enter")
        print('')

        for c in range(num):
            rest = (num + 1) - (c + 1)
            pyautogui.typewrite(txt)
            pyautogui.press("enter")
            print('Faltam {} mensagem(s)'.format(rest))

        pyautogui.typewrite('Fim do ciclo de funcionamento do bot. Todas as mensagens a partir daqui ja foram carregadas pelo bot e estao terminando de ser enviadas')
        pyautogui.press("enter")
    
    else:
        perguntas()

perguntas()