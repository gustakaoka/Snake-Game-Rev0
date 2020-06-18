pontos=0
fPontos=0

class Placar(object):
    global pontos
    global velCobrinha
    def __init__(self):
       pass
       
    def total(self):
        global pontos
        global fPontos
        global velCobrinha
        if fPontos==0:
            fPontos=1
            pontos=0
            fill(255)
            rect(75,605,60,30)
            fill(0) 
            textSize(18)
            text(pontos, 80, 625)
        else:    
            pontos += 1
            print(pontos)
            fill(255)
            rect(75,605,60,30)
            fill(0) 
            textSize(18)
            text(pontos, 80, 625)
        
        velCobrinha = pontos
        
        if(velCobrinha<10):
            frameRate(8)
        else:
            velCobrinha = int((pontos/10)+8)        
            frameRate(velCobrinha)  
            print ("velo: " ,velCobrinha )
    
    def lerTotalPontos(self):
        global pontos
        return pontos
   
def reset():
    global pontos
    pontos =0     
