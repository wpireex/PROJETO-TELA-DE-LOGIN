import PySimpleGUI as sg

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='Usuário')],
    [sg.Text('Senha')],
    [sg.Input(key='Senha')],
    [sg.Button('Login')],
    [sg.Text('', key='Mensagem')],
]

window = sg.Window('Login',layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        usuario = values['usuario']
        senha = values['senha']