#Este código é uma tentativa de automatizar a procura, manutenção e exclusão de ramais
import time
from cProfile import label
from cgitb import text
from email import message
from email.mime import image
from multiprocessing.connection import wait
from posixpath import sep
from textwrap import wrap
from time import time
from tkinter import *
import os
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from turtle import width


war = 'Não foi possivel localizar a pasta Atacchi, verifique a escrita ou se há uma pasta'
def findLogic():
    entradaUse = entrada.get().upper()
    entradauseevery = entradaUse.lower()
    os.chdir(r"G:\ATTACH")
    lista = os.listdir()
    str_match = list(filter(lambda x: f'{entradaUse and entradauseevery}' in x, lista))
    print(str_match)

    if str_match == []:
         messagebox.showerror('Usuário não encontrado.', 'Não foi possivel localizar a Pasta Atacchi')
    else:
        messagebox.showinfo('Resultados da busca', f'Foram encontrados os seguintes usuários {str_match}')


def find():
    entradaUse = entrada.get().upper()
    
    if entradaUse == '':
        confirm = messagebox.askquestion(title='Deseja Prosseguir ?', message='Isso irá mostrar todos as pastas presentes no diretorio Attachi')
        if confirm == 'no':
            exit()
            
        else:   
           findLogic()
           
    findLogic()
def test():
    delAlert = messagebox.askquestion('Atenção', 'Isso excluirá todos os dados da Pasta Attachi do usuário, deseja prosseguir ?')
    
    if  delAlert == "yes":
        try:
            os.chdir(r"G:\ATTACH")
            os.rmdir(f"{entrada.get()}")
        except:
            window_aviso = Label(window, text= war, justify=CENTER, fg='#ff0000')
            window_aviso.place(x=45,y=220)

            
    else:
        print('aborted')
    
        

window = Tk()
window.geometry("500x300")
window.title("Exclusão de  Attachi")
window.maxsize(width=500, height=300)
window.minsize(width=500, height=300)




window_orientacao = Label(window, text='Digite abaixo o Atacchi, e escolha a função.')
window_orientacao.place(x=140, y=50)
entrada = Entry(window)
entrada.place(x=180, y=100)
bt = Button(window, text="Deletar", width=20, command=test, fg='red')
bt2 = Button(window, text="Procurar", width=20, command=find, )
bt2.place(x=90, y=180)
bt.place(x=260, y=180)




window.mainloop()


