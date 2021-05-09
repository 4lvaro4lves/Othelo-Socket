from tkinter import *
from socket import *
import threading
import time
print ("SERVIDOR\n\n\n")
##############################################################################################################################
#configuração servidor

meuHost = '127.0.0.1'
minhaPort = 50007
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((meuHost, minhaPort))
sockobj.listen(5)
conexão, endereço = sockobj.accept()


###
def recebe():
    while (True):
        data = conexão.recv(1024)
        print (data.decode())
        #Label(janelaPrincipal, text='çkljhgfh').place(x=360, y=250)

###
def envia():
    resposta = nome+':> '+cxTexto.get("1.0","end-1c")
    if (cxTexto.get("1.0","end-1c") != ''):
        conexão.send(resposta.encode())
##############################################################################################################################
#configuração jogo
janelaPrincipal = Tk()
janelaPrincipal.geometry("650x450")
janelaPrincipal.resizable(width=0, height=0)
janelaPrincipal.title("Jogo Othello(Reversi) com Sockets - SERVIDOR")
nome=input("Digite seu nome: ")
imagemVerde = PhotoImage(file="imagemVerde.png")
imagemVermelha = PhotoImage(file="imagemVermelha.png")
imagemReferencia=64*[0]

global contVerde, contVermelho
contVerde = 0
contVermelho = 0
msgTela = ''

##############################################################################################################################
#configuração da aparencia do chat
def enviarMSG():
    Nome=nome+":> "
    texto = Label(janelaPrincipal, text='                                                                 ').place(x=360, y=150)
    resultado=Nome+cxTexto.get("1.0","end-1c")
    texto = Label(janelaPrincipal, text=resultado).place(x=360, y=150)
    print(resultado)
    envia()
    
cxTexto=Text(janelaPrincipal, height=5,width=35)
cxTexto.place(x=360, y=0)
btEviarMSG=Button(janelaPrincipal, height=1, width=40, text="Enviar", command=enviarMSG).place(x=360, y=85)



###


##############################################################################################################################
#configuração dos botões do jogo
def btpress11():
  pass
def btpress12():
  pass
def btpress13():
  pass
def btpress14():
  pass
def btpress15():
  pass
def btpress16():
  pass
####################botão da casa 1x7
def btpress17():
    global contVerde ,contVermelho
    if (imagemReferencia[6] == 0):
        imagemReferencia[6] = imagemVerde
        contVerde = contVerde+1
        
    elif (imagemReferencia[6] == imagemVerde):
        imagemReferencia[6] = imagemVermelha
        contVerde -= 1
        contVermelho += 1
        
    elif (imagemReferencia[6] == imagemVermelha):
        imagemReferencia[6] = imagemVerde
        contVermelho -= 1
        contVerde += 1
    bt17 = Button(janelaPrincipal,width=5,height=3,bg='black', command=btpress17,image=imagemReferencia[6]).place(x=270, y=315)
    if (contVerde + contVermelho == 64):
        if (contVerde > contVermelho):#Verde Ganhou
            vencedor(0)
        elif(contVerde < contVermelho):#Vermelho Ganhou
            vencedor(1)
        else: #Empate
            vencedor(2)
    print (contVerde,contVermelho)

####################botão da casa 1x8
def btpress18():
    global contVerde ,contVermelho
    if (imagemReferencia[7] == 0):
        imagemReferencia[7] = imagemVerde
        contVerde = contVerde+1
        
    elif (imagemReferencia[7] == imagemVerde):
        imagemReferencia[7] = imagemVermelha
        contVerde -= 1
        contVermelho += 1
        
    elif (imagemReferencia[7] == imagemVermelha):
        imagemReferencia[7] = imagemVerde
        contVermelho -= 1
        contVerde += 1
    bt18 = Button(janelaPrincipal,width=5,height=3,bg='black', command=btpress18,image=imagemReferencia[7]).place(x=315, y=315)
    if (contVerde + contVermelho == 64):
        if (contVerde > contVermelho):#Verde Ganhou
            vencedor(0)
        elif(contVerde < contVermelho):#Vermelho Ganhou
            vencedor(1)
        else: #Empate
            vencedor(2)
        
    print (contVerde,contVermelho)

##############################################################################################################################
#Linha8
bt81 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=0, y=0)
bt82 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=45, y=0)
bt83 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=90, y=0)
bt84 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=135, y=0)
bt85 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=180, y=0)
bt86 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=225, y=0)
bt87 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=270, y=0)
bt88 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=315, y=0)
#Linha7
bt71 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=0, y=45)
bt72 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=45, y=45)
bt73 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=90, y=45)
bt74 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=135, y=45)
bt75 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=180, y=45)
bt76 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=225, y=45)
bt77 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=270, y=45)
bt78 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=315, y=45)
#Linha6
bt61 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=0, y=90)
bt62 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=45, y=90)
bt63 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=90, y=90)
bt64 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=135, y=90)
bt65 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=180, y=90)
bt66 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=225, y=90)
bt67 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=270, y=90)
bt68 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=315, y=90)
#Linha5
bt51 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=0, y=135)
bt52 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=45, y=135)
bt53 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=90, y=135)
bt54 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=135, y=135)
bt55 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=180, y=135)
bt56 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=225, y=135)
bt57 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=270, y=135)
bt58 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=315, y=135)
#Linha4
bt41 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=0, y=180)
bt42 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=45, y=180)
bt43 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=90, y=180)
bt44 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=135, y=180)
bt45 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=180, y=180)
bt46 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=225, y=180)
bt47 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=270, y=180)
bt48 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=315, y=180)
#Linha3
bt31 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=0, y=225)
bt32 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=45, y=225)
bt33 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=90, y=225)
bt34 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=135, y=225)
bt35 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=180, y=225)
bt36 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=225, y=225)
bt37 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=270, y=225)
bt38 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=315, y=225)
#Lnha2
bt21 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=0, y=270)
bt22 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=45, y=270)
bt23 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=90, y=270)
bt24 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=135, y=270)
bt25 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=180, y=270)
bt26 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=225, y=270)
bt27 = Button(janelaPrincipal,width=5,height=3,bg='black').place(x=270, y=270)
bt28 = Button(janelaPrincipal,width=5,height=3,bg='white').place(x=315, y=270)
#Linha1
bt11 = Button(janelaPrincipal,width=5,height=3,bg='white', command=btpress11).place(x=0, y=315)
bt12 = Button(janelaPrincipal,width=5,height=3,bg='black', command=btpress12).place(x=45, y=315)
bt13 = Button(janelaPrincipal,width=5,height=3,bg='white', command=btpress13).place(x=90, y=315)
bt14 = Button(janelaPrincipal,width=5,height=3,bg='black', command=btpress14).place(x=135, y=315)
bt15 = Button(janelaPrincipal,width=5,height=3,bg='white', command=btpress15).place(x=180, y=315)
bt16 = Button(janelaPrincipal,width=5,height=3,bg='black', command=btpress16).place(x=225, y=315)
bt17 = Button(janelaPrincipal,width=5,height=3,bg='white', command=btpress17).place(x=270, y=315)
bt18 = Button(janelaPrincipal,width=5,height=3,bg='black', command=btpress18).place(x=315, y=315)
##############################################################################################################################



receber = threading.Thread(target=recebe)
enviar = threading.Thread(target=envia, args=(janelaPrincipal))

receber.start()
##############################################################################################################################




#while (True):
    #Label(janelaPrincipal, text='çkljhgfh').place(x=360, y=250)
 

print('final de tudo')

