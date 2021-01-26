import PySimpleGUI as sg
import os.path
import cv2
from editarImagens import redimensionarImagem, binarizar_imagem, colocar_texto, colocar_tons_cinza, negativar_imagem, rotacionar_direita, rotacionar_esquerda
from editarImagens import  espelhar_horizontal, borrar_imagem, preto_branco_adapatativo
from janelas_interface import janelaBrowser, janelaEditorImagens


janela1, janela2 = janelaBrowser(), None
caminho_imagem_escolhida = ''
imagem_escolhida = None

while True:

    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break

    # Lendo as imagens do diretório.
    elif event == 'DIRETORIO':

        listaDeImagens = list()
        pasta = values['DIRETORIO']

        try:
            listaDeArquivos = os.listdir(pasta)
        except:
            listaDeArquivos = []

        for arquivo in listaDeArquivos:
            if '.png' in arquivo.lower() or '.gif' in arquivo.lower():
                listaDeImagens.append(arquivo)

        window['listaDeImagens'].update(listaDeImagens)

    # Pegando a imagem escolhida da listBox
    elif window == janela1 and event == 'listaDeImagens':
        caminho_imagem_escolhida = os.path.join(values['DIRETORIO'], values['listaDeImagens'][0])

    elif window == janela1 and event == 'OK':
        janela2 = janelaEditorImagens()
        janela1.hide()

        imagem_escolhida = cv2.imread(caminho_imagem_escolhida)
        imagem_escolhida = redimensionarImagem(imagem_escolhida)
        imgbytes = cv2.imencode(".png", imagem_escolhida)[1].tobytes()
        janela2["-IMAGE-"].update(data=imgbytes)

    elif window == janela2 and event == 'Voltar':
        janela1.un_hide()
        janela2.hide()

    elif window == janela2 and event == 'Preto e Branco':
        try:
            imagem_escolhida = binarizar_imagem(imagem_escolhida,128)
            imgbytes = cv2.imencode(".png", imagem_escolhida)[1].tobytes()
            janela2["-IMAGE-"].update(data=imgbytes)
        except:
            pass

    elif window == janela2 and event == 'Original':
        imagem_escolhida = cv2.imread(caminho_imagem_escolhida)
        imagem_escolhida = redimensionarImagem(imagem_escolhida)
        imgbytes = cv2.imencode('.png', imagem_escolhida)[1].tobytes()
        janela2['-IMAGE-'].update(data=imgbytes)

    elif window == janela2 and event == 'Texto':
        texto = sg.popup_get_text('Informe o Texto: ')
        posicao = sg.popup_get_text('Informe a posiição no formato (x,y) sem espaços: ')
        imagem_escolhida = colocar_texto(imagem_escolhida,texto,posicao)
        imgbytes = cv2.imencode('.png', imagem_escolhida)[1].tobytes()
        janela2['-IMAGE-'].update(data=imgbytes)

    elif window == janela2 and event == 'Tons de cinza':
        try:
            imagem_escolhida = colocar_tons_cinza(imagem_escolhida, caminho_imagem_escolhida)
        except:
            pass

        imgbytes = cv2.imencode('.png', imagem_escolhida)[1].tobytes()
        janela2['-IMAGE-'].update(data=imgbytes)

    elif window == janela2 and event == 'Negativar':
        try:
            imagem_escolhida = negativar_imagem(imagem_escolhida, caminho_imagem_escolhida)
        except:
            pass

        imgbytes = cv2.imencode('.png', imagem_escolhida)[1].tobytes()
        janela2['-IMAGE-'].update(data=imgbytes)

    elif window == janela2 and event == 'Rot.\nRight':
        imagem_escolhida = rotacionar_direita(imagem_escolhida)
        imgbytes = cv2.imencode('.png', imagem_escolhida)[1].tobytes()
        janela2['-IMAGE-'].update(data=imgbytes)

    elif window == janela2 and event == 'Rot.\nLeft':
        imagem_escolhida = rotacionar_esquerda(imagem_escolhida)
        imgbytes = cv2.imencode('.png', imagem_escolhida)[1].tobytes()
        janela2['-IMAGE-'].update(data=imgbytes)

    elif window == janela2 and event == 'Espelhar':
        imagem_escolhida = espelhar_horizontal(imagem_escolhida)
        imgbytes = cv2.imencode('.png', imagem_escolhida)[1].tobytes()
        janela2['-IMAGE-'].update(data=imgbytes)

    elif window == janela2 and event == 'Borrar':
        imagem_escolhida = borrar_imagem(imagem_escolhida)
        imgbytes = cv2.imencode('.png', imagem_escolhida)[1].tobytes()
        janela2['-IMAGE-'].update(data=imgbytes)

    elif window == janela2 and event == 'Preto e branco\nAdaptativo':
        imagem_escolhida = preto_branco_adapatativo(imagem_escolhida)
        imgbytes = cv2.imencode('.png', imagem_escolhida)[1].tobytes()
        janela2['-IMAGE-'].update(data=imgbytes)

window.close()

