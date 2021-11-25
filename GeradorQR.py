import pyqrcode
import PySimpleGUI as sg

sg.theme('DarkBlue3')  #criando a janela
layout = [
    [sg.Text('Gerador de QR Code', font=('bold', 16))],
    [sg.Text('_______________________________________________')],
    [sg.Text('Insira aqui o link', font=13), sg.Input(key='link')],
    [sg.Text('Escolha o nome do arquivo', font=13), sg.Input(key='nome_arquivo')],
    [sg.Text('Escolha onde Salvar >>>', font=13), sg.FolderBrowse(key='destino')],
    [sg.Text('_______________________________________________')],
    [sg.Button('Gerar QrCode'), sg.Button('Sair')],
    [sg.Text('Se gostou do programa e quiser incentivar o desenvolvedor, faça uma doação.')],
    [sg.Text('Pix: lopes.laerte@gmail.com')],
    [sg.Text('Desenvolvido por: Laerte Lopes')]

]
janela = sg.Window("Gerador de QR code Milerte v1.1", layout=layout, element_justification='center')

while True:  # criando eventos
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Sair':
        break
    if eventos == 'Gerar QrCode':
        diretorio = valores['destino']
        nomearquivo = valores['nome_arquivo']
        url = pyqrcode.create(valores['link'])  #convertendo o link em QR
        url.png(f'{diretorio}' + f'./{nomearquivo}.png', scale=5)  #convertendo em PNG
        sg.popup('Seu QRCode foi gerado com sucesso')
