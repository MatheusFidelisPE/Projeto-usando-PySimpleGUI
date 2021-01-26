import cv2
caminho_imagem_escolhida  = ''

def redimensionarImagem(imagem):
    largura = imagem.shape[1]
    altura = imagem.shape[0]
    novaLargura = 500
    coef = novaLargura/altura

    imagem = cv2.resize(imagem,(int(largura*coef),int(novaLargura)))
    return imagem

def binarizar_imagem(imagem, valor):
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2LAB)[:, :, 0]
    imagem = cv2.threshold(imagem, valor, 255, cv2.THRESH_BINARY)[1]
    return imagem


def carregarImagemPrincipal(diretorio):
    imagem_escolhida = cv2.imread(diretorio)
    imagem_escolhida = redimensionarImagem(imagem_escolhida)
    return  imagem_escolhida


def colocar_texto(imagem, texto, posicao):
    try:
        posicao = posicao.replace(' ','')
        posicao = posicao.replace('(', '')
        posicao = posicao.replace(')', '')
        posicao1, posicao2 = posicao.split(',')
        posicao1 = int(posicao1)
        posicao2 = int(posicao2)
        fonte = cv2.FONT_HERSHEY_PLAIN
        imagem = cv2.putText(imagem, texto,(posicao1, posicao2), fonte, 2, (255,255,255), 2,cv2.LINE_AA)
    except:
        pass
    return imagem


def colocar_tons_cinza(imagem= None, imagem_caminho = ''):

    try:
        imagem = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
    except:
        imagem = cv2.imread(imagem_caminho)
        imagem = cv2.cvtColor(imagem)

    return imagem

def negativar_imagem(imagem, imagem_caminho):
    try:
        imagem = cv2.cvtColor(imagem,cv2.COLOR_BGR2HSV)
    except:
        imagem = cv2.imread(imagem_caminho)
        imagem = cv2.cvtColor(imagem)

    return imagem


def rotacionar_direita(imagem):
    (alt, lar) = imagem.shape[:2]  # captura altura e largura
    centro = (lar // 2, alt // 2)  # acha o centro
    mascara = cv2.getRotationMatrix2D(centro, -90,1.0)
    imagem = cv2.warpAffine(imagem,mascara,(lar,alt))

    return imagem



def rotacionar_esquerda(imagem):
    (alt, lar) = imagem.shape[:2]  # captura altura e largura
    centro = (lar // 2, alt // 2)  # acha o centro
    mascara = cv2.getRotationMatrix2D(centro, 90,1.0)
    imagem = cv2.warpAffine(imagem,mascara,(lar,alt))

    return imagem


def espelhar_horizontal(imagem):
    imagem = cv2.flip(imagem, 1)
    return imagem


def borrar_imagem(imagem):
    imagem_borrada = cv2.GaussianBlur(imagem, (7, 7), 0)
    return imagem_borrada


def preto_branco_adapatativo(imagem):
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem = borrar_imagem(imagem)
    bin2 = cv2.adaptiveThreshold(imagem, 255,
                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,
                                 21, 5)
    return bin2

