import pyqrcode
from pyqrcode import QRCode
import png
from PySimpleGUI import *

theme('Reddit')

telaURL = [
    [Text('Link:                  '), Input(key = 'link')],
    [Text('Nome do arquivo:'), Input(key = 'file')],
    [Button('Gerar')]
]

tu = Window('Gerador de QRCODE', telaURL)

while True:
    e, v = tu.Read()

    if e == WINDOW_CLOSED:
        break

    if e == 'Gerar':
        qrString = v['link']
        name = v['file']
        arquivo = f'{name}.png'
        url = pyqrcode.create(qrString)
        url.png(arquivo, scale = 8)
        tu.Close()

        telaImagem = [
            [Image(arquivo)]
        ]

        ti = Window('QRCODE', telaImagem)
    
    while True:
        e, v = ti.Read()

        if e == WINDOW_CLOSED:
            break