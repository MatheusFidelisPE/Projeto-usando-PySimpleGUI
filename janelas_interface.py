import PySimpleGUI as sg


def janelaBrowser():

    layout = [
        [sg.Text('Selecione a Imagem:')],
        [sg.In(enable_events=True, size=(30,1), key='DIRETORIO'), sg.FolderBrowse()],
        [sg.Listbox(values= [],enable_events=True, size = (40,10),key='listaDeImagens')],
        [sg.Button('OK')]
    ]
    return sg.Window('Editor de Imagens', layout= layout, finalize=True)


def janelaEditorImagens():

    layoutBody1 = [
        [
            sg.Button('Original',size=(15,1))
        ],
        [
            sg.Button('Tons de cinza',size=(15,1))
        ],
        [
            sg.Button('Negativar',size=(15,1))
        ],
        [
            sg.Button('Rot.\nRight',size=(7,2)),sg.Button('Rot.\nLeft',size=(6,2))
        ],
        [
            sg.Button('Texto',size=(15,1))
        ],
        [
            sg.Button('Preto e Branco',size=(15,1))
        ],
        [
            sg.Button('Espelhar',size=(15,1))
        ],
        [
            sg.Button('Rotacionar',size=(15,1))
        ],
        [
            sg.Button('Preto e branco\nAdaptativo', size=(15, 2))
        ],
        [
            sg.Button('Borrar', size=(15, 1))
        ],
    ]

    layoutBody2 = [
        [sg.Image(filename='', key='-IMAGE-')],

    ]
    layoutBodyFim = [
        [
            sg.Text('Tela de edição                                                                                                                                                                          '),
            sg.Button('Voltar'), sg.Button('Salvar'),
        ],

        [
            sg.Column(layoutBody1),
            sg.VSeparator(),
            sg.Column(layoutBody2),
        ]
    ]
    return sg.Window('Procura de imagens', layout= layoutBodyFim, finalize=True)