from comida import Comida
from cobrinha import Cobrinha
from statusJogo import StatusJogo
import cobrinha
import template
import pontos 

controle2=0 
controle=0

def setup():
    global fControle
    size(620,640)  
    fControle=0
    template.iniciar()
     
def draw():
    global controle
    global controle2
    global fControle
    
    if controle2 != 0:
        controle=controle2
        
    if controle==0:
        template.home()
        template.corCobrinha()    
        if(mousePressed and mouseX>210 and mouseX<410 and mouseY>250 and mouseY<334):
            controle=1
    
    if(controle==1):
        if fControle==0:
            
            status = StatusJogo()
            status.inicio() 
            template.iniciar()
            fControle=1
        else:    
            jogo()

    if (controle==2):
        template.fim()
        if(mousePressed and mouseX>205 and mouseX<421 and mouseY>270 and mouseY<340):
            pontos.reset()
            controle=0
            fControle=0
            controle2=0
            snack = Comida()
            snack.atualiza()

def jogo():
    global controle2
       
    Cobra = Cobrinha()
    controle2=Cobra.sentido()
    snack = Comida()
    snack.atualiza()
   
