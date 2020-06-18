from cobrinha import Cobrinha
from cobrinha import vetorCobrinha
from cobrinha import coordenadasCobrinhaX
from cobrinha import coordenadasCobrinhaY
from pontos import Placar
import cobrinha
import pontos

global escala
global fSetupInicio
global controle3Anterior
fSetupInicio=0
controle3Anterior=0
escala=20 #DEVE ser PAR (trocar na aba cobrinha a mesma variavel)



vetorComida = [escala*int(random(escala/10,600/escala)),escala*int(random(escala/10,600/escala))]

def setupInicio():
    global fComida
    fComida=0

class Comida(object):
    def __init__(self):
        pass
    
    def atualiza(self):
        global vetorCobrinha
        global vetorComida
        global fComida
        global fSetupInicio
        global controle3Anterior
        global controle3
        
        if fSetupInicio==0:
            setupInicio()
            fSetupInicio=1
        
        controle3=cobrinha.controle() #reseta a comida no fim do jogo
        
        print 'ctrl3',controle3
        if(controle3==2):
            #controle3=0
            fComida=0
            estado('desliga')
             
        else:     
            if(vetorCobrinha() != vetorComida and fComida==0 and controle3==0):
                estado('liga')
                fComida=1        
            elif(vetorCobrinha() == vetorComida and fComida==1 and controle3==0):
                fComida=0
        
        print 'controle3', controle3, 'controle3Anterior', controle3Anterior
     
        controle3Anterior=controle3
                 
def estado(fazer): 
    global vetorComida
    global escala        
    global fRandom
    global controle3
    global controle3Anterior
    img6 = loadImage("maca.jpg") 
    placar=Placar()
    pontos=placar.lerTotalPontos()
      
    fRandom=0
    
   
    if (fazer=='liga'):
        while(fRandom==0):
            vetorComida = [escala*int(random(1,600/escala)),escala*int(random(1,600/escala))]
            fRandom=1
            for j in range(1,pontos+1,+1):
                if(vetorComida[0]==coordenadasCobrinhaX()[j] and vetorComida[1]==coordenadasCobrinhaY()[j]):
                    fRandom=0    
        
        image(img6,vetorComida[0],vetorComida[1],escala,escala) #maca image
        
        if controle3Anterior!= controle3:
            print 'paaassei aquiii'
            fill(255)
            rect(75,605,60,30)
            fill(0) 
            textSize(18)
            text(0, 80, 625)
            pass
        else:    
            placar = Placar()
            placar.total()
        
