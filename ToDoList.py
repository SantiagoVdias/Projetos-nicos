# Projeto To Do List por Santiago Dias
# Idéia: Checkbox e imput com o nome de cada tarefa ; Botão de adicionar tarefa ; Botão de resetar

import PySimpleGUI as sg

# Criação do layout

def criar_janela_inicial():          # Abre uma função da janela
    sg.theme('DarkBlue4')            # Define o tema da janela
    linha = [
        [sg.Checkbox(''), sg.Input('')] # linha inicial do código

    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha,key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

    return sg.Window('To Do List',layout=layout,finalize=True)

# Criar a janela

janela = criar_janela_inicial()

# Regras da janela

while True:
    event, value = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()