from tkinter import font
from tkinter.ttk import Style
from turtle import width
from typing_extensions import Self
from Usuarios import Usuarios
from tkinter import *
import mysql.connector
# pip install mysql-connector-python
# pip install typing-extensions

class Application:
    def __init__(self, master=None):
        self.fonte=("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"]=10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"]=20
        self.container2["pady"]=5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"]=20
        self.container3["pady"]=5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"]=20
        self.container4["pady"]=5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"]=20
        self.container5["pady"]=5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"]=20
        self.container6["pady"]=5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"]=20
        self.container7["pady"]=5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"]=20
        self.container8["pady"]=10
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"]=15
        self.container9.pack()

        self.titulo = Label(self.container1,text="Informe os dados: ")
        self.titulo["font"] = ("Calibri","9","bold")
        self.titulo.pack()

        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"]=25
        self.txtnome["font"]=self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblemail = Label(self.container4, text="Email:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container4)
        self.txtemail["width"]=25
        self.txtemail["font"]=self.fonte
        self.txtemail.pack(side=LEFT)

        self.lbltelefone = Label(self.container5, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(self.container5)
        self.txttelefone["width"]=25
        self.txttelefone["font"]=self.fonte
        self.txttelefone.pack(side=LEFT)

        self.lblendereco = Label(self.container6, text="Endereço:", font=self.fonte, width=10)
        self.lblendereco.pack(side=LEFT)

        self.txtendereco = Entry(self.container6)
        self.txtendereco["width"]=25
        self.txtendereco["font"]=self.fonte
        self.txtendereco.pack(side=LEFT)

        self.lblsenha = Label(self.container7, text="Senha: ", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"]=25
        self.txtsenha["show"]="*"
        self.txtsenha["font"]=self.fonte
        self.txtsenha.pack(side=LEFT)

        self.btnInsert = Button(self.container8, text="Confirmar Cadastro", font=self.fonte, width=16)
        self.btnInsert["command"]=self.cadastroUsuario
        self.btnInsert.pack(side=LEFT)  

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana","9","italic")
        self.lblmsg.pack()

        self.conectarBanco()

    def conectarBanco(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "loja_de_tenis"
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
        cliente(
            cd_cliente INT AUTO_INCREMENT PRIMARY KEY,
            nome TEXT,
            telefone TEXT,
            email TEXT,
            endereco TEXT,
            senha TEXT)''')
        
        self.conn.commit()
    
    def cadastroUsuario(self):
        nome = self.txtnome.get()
        email = self.txtemail.get()
        telefone = self.txttelefone.get()
        endereco = self.txtendereco.get()
        senha = self.txtsenha.get()
        self.cursor.execute("INSERT INTO cliente(nome, email, telefone, endereco, senha)VALUES(%s,%s,%s,%s,%s)",
                            (nome,email,telefone,endereco,senha))
        self.conn.commit()
        self.lblmsg["text"]="Você se cadastrou!"
        self.limparCampos()

    def __del__(self):
        self.conn.close()

if __name__=="__main__":
    root = Tk()
    Application(root)   
    root.mainloop()