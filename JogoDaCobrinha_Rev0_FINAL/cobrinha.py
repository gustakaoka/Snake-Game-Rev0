from statusJogo import StatusJogo
from pontos import Placar
import template

global vetorCobrinha
global vetorCobrinhaAnterior
global direcao
global pontos
global pontoAnterior
global escala
global coordenadasCobrinhaX
global coordenadasCobrinhaY
global fSetupInicio
global corCobrinhaR 
global corCobrinhaG
global corCobrinhaB
fSetupInicio=0

escala=20 #DEVE ser PAR (trocar na aba comida a mesma variavel)

    
def setupInicioCobrinha():
    global coordenadasCobrinhaX
    global coordenadasCobrinhaY
    global direcao
    global pontoAnterior
    global pontos
    global vetorCobrinha
    global controle3
    global corCobrinhaR 
    global corCobrinhaG
    global corCobrinhaB
    
    corCobrinhaR=template.cobrinhaRCor()
    corCobrinhaG=template.cobrinhaGCor()
    corCobrinhaB=template.cobrinhaBCor()
    
    vetorCobrinha=[(escala/2)*20,(escala/2)*20]
    coordenadasCobrinhaX=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    coordenadasCobrinhaY=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    pontoAnterior=0
    pontos=0
    direcao=[0,0]
    controle3=0

class Cobrinha(object):
    def __init__(self):    
        pass
       
    def sentido(self):
        global vetorCobrinha
        global vetorCobrinhaAnterior
        global direcao
        global pontos
        global escala
        global fSetupInicio
        global controle3
        global corCobrinhaR 
        global corCobrinhaG
        global corCobrinhaB
        if fSetupInicio==0:
            setupInicioCobrinha()
            fSetupInicio=1
        
        placar=Placar()
        pontos=placar.lerTotalPontos()
        atualiza_off()
    
        if (keyCode == UP and direcao != [0,1] ):
            direcao=[1,0]
        elif (keyCode == DOWN and direcao != [1,0] ):
            direcao=[0,1]
        elif (keyCode == LEFT and direcao != [0,0] ):
            direcao=[1,1]
        elif (keyCode ==RIGHT and direcao != [1,1] ):
            direcao=[0,0]
            
        status = StatusJogo()

        
        if(direcao == [1,0] and vetorCobrinha[1]>=10): #cima
            vetorCobrinha[1] = vetorCobrinha[1]-escala
            atualiza_on()
        elif(direcao == [1,0] and vetorCobrinha[1]<10): #saiu para cima
            fSetupInicio=0
            controle3=2
            return 2
                       
        if(direcao == [0,1] and vetorCobrinha[1]<=570): #baixo
            vetorCobrinha[1] = vetorCobrinha[1]+escala
            atualiza_on()
        elif(direcao == [0,1] and vetorCobrinha[1]>570): #saiu para baixo
            fSetupInicio=0
            controle3=2
            return 2
        
        if(direcao == [1,1] and vetorCobrinha[0]>=25): #esquerda
            vetorCobrinha[0] = vetorCobrinha[0]-escala
            atualiza_on()
        elif(direcao == [1,1] and vetorCobrinha[0]<25): #saiu para esquerda
            fSetupInicio=0
            controle3=2
            return 2
                                                
        if(direcao == [0,0] and vetorCobrinha[0]<=575): #direita
            vetorCobrinha[0] = vetorCobrinha[0]+escala
            atualiza_on()
        elif(direcao == [0,0] and vetorCobrinha[0]>575): #saiu para direita
            fSetupInicio=0
            controle3=2
            return 2       
        
        for j in range(1,pontos+1,+1): # perdeu porque encostou no rabo
            if(vetorCobrinha[0]==coordenadasCobrinhaX[j] and vetorCobrinha[1]==coordenadasCobrinhaY[j]):
                fSetupInicio=0
                controle3=2
                return 2     
        
        vetorCobrinhaAnterior = vetorCobrinha
        
        return 0    
            
            
def atualiza_on():
    global pontos
    global coordenadasCobrinhaX
    global coordenadasCobrinhaY
    global coordenadasCobrinhaAnterior
    global pontoAnterior
    global vetorCobrinhaAnterior
    global escala
    global corCobrinhaR
    global corCobrinhaG
    global corCobrinhaB 
    if pontos==0:
        coordenadasCobrinhaX[0]= vetorCobrinha[0]
        coordenadasCobrinhaY[0]= vetorCobrinha[1]        
    else:
        for i in range(pontos,0,-1):
            coordenadasCobrinhaX[i]=coordenadasCobrinhaX[i-1]
            coordenadasCobrinhaY[i]=coordenadasCobrinhaY[i-1]
            if i==1:
                coordenadasCobrinhaX[0]= vetorCobrinha[0]
                coordenadasCobrinhaY[0]= vetorCobrinha[1]         
            
            #print i, i-1
    stroke(168,223,73)

    fill(corCobrinhaR,corCobrinhaG,corCobrinhaB)
    rect(vetorCobrinha[0],vetorCobrinha[1],escala,escala)       

    
    #print 'CoordenadasX:', coordenadasCobrinhaX
    #print 'CoordenadasY:', coordenadasCobrinhaY

def coordenadasCobrinhaX():
    global coordenadasCobrinhaX
    return coordenadasCobrinhaX
def coordenadasCobrinhaY():
    global coordenadasCobrinhaY
    return coordenadasCobrinhaY
    
def atualiza_off():
    global coordenadasCobrinhaX
    global coordenadasCobrinhaY
    global pontos
    global escala

    if pontos==0:
        stroke(168,223,73)
        fill(168,223,73)
        rect(vetorCobrinha[0],vetorCobrinha[1],escala,escala)
    else:
        #print 'PONTOS:', pontos            
        stroke(168,223,73)
        fill(168,223,73)
        rect(coordenadasCobrinhaX[pontos],coordenadasCobrinhaY[pontos],escala,escala)
    stroke(255)
    fill(255)
    rect(0,0,19,20) 
     
def lerCoordenadasCobrinhaY(self):
    global coordenadasCobrinhaY
    return coordenadasCobrinhaY

def lerCoordenadasCobrinhaX(self):
    global coordenadasCobrinhaX
    return coordenadasCobrinhaX

def vetorCobrinha():
    global vetorCobrinha
    return vetorCobrinha           

def controle():
    global controle3
    return controle3     
