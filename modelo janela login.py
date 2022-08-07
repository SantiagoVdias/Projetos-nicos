import PySimpleGUI as sg

# Layout
sg.theme('DarkBlue4') # Define o tema
layout = [
    [sg.Text("Usuário")] ,
    [sg.Input(key='usuario')], 
    [sg.Text("Senha")], 
    [sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salver o usuário e senha')],
    [sg.Button('Entrar')],
    [sg.Text('',key='mensagem')]
]
# Janela
janela = sg.Window('Tela de Login', layout)
# Ler eventos
while True:
    events, values = janela.read()
    if events == sg.WINDOW_CLOSED:
        break
    elif events == 'Entrar':
        senha_correta = '12345'
        usuario_correto = 'Santiago'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            janela['mensagem'].update("Login feito com Sucesso!")
        else:
            janela['mensagem'].update("Usuário ou senha incorretos")