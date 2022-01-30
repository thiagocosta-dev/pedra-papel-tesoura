"""
Autor: Thiago Costa Pereira
Contatos
  Email: thiago.devpython@gmail.com
  Linkedin: https://www.linkedin.com/in/thiago-costa-pereira-b650b0228/
"""


from tkinter import *
from PIL import Image, ImageTk
from random import randint

janela = Tk()
janela.title('# Pedra Papel Tesoura #')
janela.configure(background='#c8a2c8')

#  Carregar as imagens
pedra_img = ImageTk.PhotoImage(Image.open('PedraUsuario.png'))
papel_img = ImageTk.PhotoImage(Image.open('PapelUsuario.png'))
tesoura_img = ImageTk.PhotoImage(Image.open('TesouraUsuario.png'))
pedra_img_pc = ImageTk.PhotoImage(Image.open('PedraPc.png'))
papel_img_pc = ImageTk.PhotoImage(Image.open('PapelPc.png'))
tesoura_img_pc = ImageTk.PhotoImage(Image.open('TesouraPc.png'))

#  Inserindo as imagens
label_usuario = Label(janela, image=tesoura_img, bg='#c8a2c8')
label_pc = Label(janela, image=tesoura_img_pc, bg='#c8a2c8')
label_pc.grid(row=1, column=0)
label_usuario.grid(row=1, column=4)

#  Pontuação
pont_usuario = Label(janela, text=0, font=100, bg='#c8a2c8', fg='black')
pont_pc = Label(janela, text=0, font=100, bg='#c8a2c8', fg='black')
pont_usuario.grid(row=1, column=3)
pont_pc.grid(row=1, column=1)

#  Indicadores
ind_usuario = Label(janela, font=50, text='USUÁRIO', bg='#FFFFFF', fg='black')
ind_pc = Label(janela, font=50, text='COMPUTADOR', bg='#FFFFFF', fg='black')
ind_usuario.grid(row=0, column=3)
ind_pc.grid(row=0, column=1)

#  Mensagens
msg = Label(janela, font=50, bg='#FFFFFF', fg='black')
msg.grid(row=1, column=2)


#  Atualizando Mensagem
def atualizando_msg(x):
    msg['text'] = x


#  Atualizando pontuação usuário
def pontos_usuario():
    ponto = int(pont_usuario['text'])
    ponto += 1
    pont_usuario['text'] = str(ponto)


#  Atualizando pontuação Pc
def pontos_pc():
    ponto = int(pont_pc['text'])
    ponto += 1
    pont_pc['text'] = str(ponto)


#  Checando vencedor
def vencedor(usuario, pc):
    if usuario == pc:
        atualizando_msg('Empate!!')
    elif usuario == 'pedra':
        if pc == 'papel':
            atualizando_msg('Você perdeu!!')
            pontos_pc()
        else:
            atualizando_msg('Você Ganhou!!')
            pontos_usuario()
    elif usuario == 'papel':
        if pc == 'tesoura':
            atualizando_msg('Você perdeu!!')
            pontos_pc()
        else:
            atualizando_msg('Você ganhou!!')
            pontos_usuario()
    elif usuario == 'tesoura':
        if pc == 'pedra':
            atualizando_msg('Você perdeu!!')
            pontos_pc()
        else:
            atualizando_msg('Você ganhou!!')
            pontos_usuario()
    else:
        pass


#  Atualizando escolhas
escolha = ['pedra', 'papel', 'tesoura']


def atualizando_escolhas(x):
    #  Para PC
    escolha_pc = escolha[randint(0, 2)]
    if escolha_pc == 'pedra':
        label_pc.configure(image=pedra_img_pc)
    elif escolha_pc == 'papel':
        label_pc.configure(image=papel_img_pc)
    else:
        label_pc.configure(image=tesoura_img_pc)

    #  Para usuário

    if x == 'pedra':
        label_usuario.configure(image=pedra_img)
    elif x == 'papel':
        label_usuario.configure(image=papel_img)
    else:
        label_usuario.configure(image=tesoura_img)

    vencedor(x, escolha_pc)


#  Botões
pedra = Button(janela, width=20, height=2, text='PEDRA', bg='#FFFFFF', fg='black',
               command=lambda: atualizando_escolhas('pedra'))
papel = Button(janela, width=20, height=2, text='PAPEL', bg='#FFFFFF', fg='black',
               command=lambda: atualizando_escolhas('papel'))
tesoura = Button(janela, width=20, height=2, text='TESOURA', bg='#FFFFFF', fg='black',
                 command=lambda: atualizando_escolhas('tesoura'))
pedra.grid(row=2, column=1)
papel.grid(row=2, column=2)
tesoura.grid(row=2, column=3)

janela.mainloop()
