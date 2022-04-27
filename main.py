import PySimpleGUI as sg

def enviar():
    item = float('valor')


#enviar()


sg.theme('Reddit')


layout = [
    [sg.Text('Responda as questões abaixo e veja se vale apena a sua compra')],
    [sg.Checkbox('Eletrônico', key='eletronico')],
    [sg.Checkbox('Eletrodoméstico', key='eletrodomestico')],
    [sg.Checkbox('Item de cozinha', key='item_de_cozinha')],
    [sg.Checkbox('Diversão', key='diversao')],
    [sg.Text('Agora digite o valor estimado da compra')],
    [sg.Input('', key='valor')],
    [sg.Button('Enviar', key='enviar')],
    [sg.Text('', key='resultado')]
]


janela = sg.Window('Teste', layout)

while True:
    evento, valores = janela.read()

    if evento == sg.WINDOW_CLOSED:
        break

    elif evento == 'enviar' and valores['eletronico'] and float(janela['valor'].get()) > 4000:
        janela['resultado'](f'Esse foi o valor estimado {janela["valor"].get()}, que tal repensar sobre essa compra?')
    elif evento == 'enviar' and valores['eletrodomestico'] and float(janela['valor'].get()) > 5000:
        janela['resultado'](f'Esse foi o valor estimado {janela["valor"].get()}, que tal procurar uma opção mais barata?')
    elif evento == 'enviar' and valores['item_de_cozinha'] and float(janela['valor'].get()) > 1500:
        janela['resultado'](f'Esse foi o valor estimado {janela["valor"].get()}, sim, está caro, porém repensar é o mais importante')
    elif evento == 'enviar' and valores['diversao'] and float(janela['valor'].get()) > 2000:
        janela['resultado'](f'Esse foi o valor estimado {janela["valor"].get()}, Você precisa gastar tudo isso mesmo?')
    else:
        janela['resultado'](f'Parabéns')