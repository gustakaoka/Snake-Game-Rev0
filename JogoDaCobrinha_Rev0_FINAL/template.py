import pontos 

global cobrinhaR
global cobrinhaG
global cobrinhaB
global fCor

fCor=0

def iniciar():  
    fill(0) 
    textSize(18)
    text("Score: ", 20, 625)
    
    fill(0) 
    textSize(14)
    text("Author: TAKAOKA,G. - Brazil ", 400, 625)
    
   

def home():
    stroke(165,237,242)
    fill(165,237,242)
    rect(10,0,600,600)
    img6 = loadImage("snakeInicio2.jpg")
    image(img6, 10, 350,600,250) #snakeinicio image 
    img5 = loadImage("sol.jpg")
    image(img5, 10, 10,600,270) #sun image         
    img7 = loadImage("play.jpg")
    image(img7, 210, 250,200,84) #play image 
    
        
def fim():
    img = loadImage("gameover.jpg")
    img2 = loadImage("electronic.jpg")
    img3 = loadImage("snake2.jpg")
    img4 = loadImage("restart.jpg")
     
    stroke(237,27,36)
    fill(237,27,36)
    rect(10,0,600,600)
    
    image(img4, 205, 270,216,70) #restart image 
    image(img, 180, 160,266,56) #gameover image    
    image(img2, 20, 15,278,65) #electronic image 
    image(img3, 10, 350,601,251) #snake image  
    
    fill(0) 
    textSize(17)
    text("2020.06 Rev0.0", 475, 20)
    
    fill(0) 
    textSize(25)
    text("Score:", 255, 245)
    text(pontos.pontos, 337, 245)
    
def inicio():
    stroke(168,223,73)
    background(255)
    fill(168,223,73)
    rect(20,0,580,600) 

def corCobrinha():
    global cobrinhaR
    global cobrinhaG
    global cobrinhaB
    global fCor
    
    fill(6,115,142)
    rect(9,605,230,30)
    fill(255) 
    textSize(16)
    text('Snake Color:', 18, 626)
    fill(255)
    rect(130,610,20,20)    
    fill(0,255,150)
    rect(170,610,20,20)
    fill(150,120,150)
    rect(210,610,20,20)
    if(mousePressed and mouseX>130 and mouseX<150 and mouseY>610 and mouseY<630):
        cobrinhaR=255
        cobrinhaG=255
        cobrinhaB=255
        stroke(0)
        noFill()
        rect(130,610,20,20)
        fCor=1
    elif(mousePressed and mouseX>170 and mouseX<190 and mouseY>610 and mouseY<630):
        cobrinhaR=0
        cobrinhaG=255
        cobrinhaB=150
        stroke(0)
        noFill()
        rect(170,610,20,20)
        fCor=1            
    elif(mousePressed and mouseX>210 and mouseX<230 and mouseY>610 and mouseY<630):
        cobrinhaR=150
        cobrinhaG=120
        cobrinhaB=150
        stroke(0)
        noFill()
        rect(210,610,20,20)
        fCor=1
    elif fCor==0:
        cobrinhaR=255
        cobrinhaG=255
        cobrinhaB=255        
        
def cobrinhaRCor():
    global cobrinhaR
    return cobrinhaR
def cobrinhaGCor():
    global cobrinhaG
    return cobrinhaG
def cobrinhaBCor():
    global cobrinhaB
    return cobrinhaB
