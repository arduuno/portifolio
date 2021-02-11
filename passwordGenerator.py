from random import sample
from PySimpleGUI import *

theme('Reddit')

#CARACTERES POSSÍVEIS
minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABCDEFGHIJKLMNOPQRST'
numeros = '0123456789'
simbolos = '!@#$%&*()-=+{[]},.;:></?\_'


#DECLARAÇÃO DAS VARIÁVEIS DOS DADOS
nome = ''
senha = ''
tamanho = 0
soma = ''


#LAYOUT DA GUI
tela = [
    [Text('Título da senha:          '), Input(key = 'nome')],
    [Text('Número de caracteres:'), Input(key = 'numCaracs')],
    [Text('Sua senha deve conter:')],
    [Checkbox('Letras maiúsculas', key = 'masc')],
    [Checkbox('Letras minúsculas', key = 'minusc')],
    [Checkbox('Números', key = 'nums')],
    [Checkbox('Caracteres especiais', key = 'simb')],
    [Button('Gerar')],
    [Output(size = (65, 0))]
]


#MÉTODO PARA GERAÇÃO DA SENHA
def geraSenha(nome, tamanho, caracteres):
    senha = ''.join(sample(caracteres, tamanho))
    print(f'''




    
    {senha}
    ''')

    file = open('senhas.txt', 'a')
    file.write(f'Nome: {nome} || Senha: {senha}\n')
    file.close()
    


#CRIAÇÃO DA TELA E FUNCIONAMENTO DA MESMA
tl = Window('Gerador de senhas', tela)

while True:
    e, v = tl.Read()
    nome = v['nome']
    tamanho = v['numCaracs']
    

    if e == WINDOW_CLOSED:
        break

    if e == 'Gerar':
        if nome == '' or tamanho == '':
            popup_error('Preencha todos os campos')
        
        else:
            if v['simb'] == False and v['nums'] == False and v['minusc'] == False and v['masc'] == False:
                popup_error('Marque alguma opção')
            
            else:
                tamanho = int(tamanho)
            
                if v['masc'] == True:
                    soma += maiusculas
                
                if v['minusc'] == True:
                    soma += minusculas
                
                if v['nums'] == True:
                    soma += numeros

                if v['simb'] == True:
                    soma += simbolos
                
                
                
                geraSenha(nome, tamanho, soma)
                soma = ''
                senha = ''

