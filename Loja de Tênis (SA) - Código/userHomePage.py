from ctypes import sizeof
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage  

jan = Tk()
jan.title("Loja de Tenis NIKE")
jan.geometry("1632x918")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 1)
jan.iconbitmap(default="icons/nike.ico")

Tenis1 = PhotoImage(file="icons/Tenis1.png")
Frame = Frame(jan, width=1632, height=918, bg="lightblue", relief="raise")
Frame.pack(side=LEFT)
LogoLabel1 = Label(Frame, image=Tenis1, bg="white")
LogoLabel1.place(x=300, y=150)
TextoTenis1 = Label(Frame,text="Exemplo Tenis 1",font = "Arial",bg="White")
TextoTenis1.place(x=335,y=300)
TextoTenis1 = Label(Frame,text="R$:500,00",font = "Arial",bg="White")
TextoTenis1.place(x=355,y=330)

Tenis2 = PhotoImage(file="icons/Tenis2.png")
LogoLabel1 = Label(Frame, image=Tenis2, bg="white")
LogoLabel1.place(x=550, y=150)
TextoTenis2 = Label(Frame,text="Exemplo Tenis 2",font = "Arial",bg="White")
TextoTenis2.place(x=585,y=300)
TextoTenis2 = Label(Frame,text="R$:285,00",font = "Arial",bg="White")
TextoTenis2.place(x=605,y=330)

Tenis3 = PhotoImage(file="icons/Tenis3.png")
LogoLabel1 = Label(Frame, image=Tenis3, bg="white")
LogoLabel1.place(x=800, y=150)
TextoTenis3 = Label(Frame,text="Exemplo Tenis 3",font = "Arial",bg="White")
TextoTenis3.place(x=835,y=300)
TextoTenis3 = Label(Frame,text="R$:300,00",font = "Arial",bg="White")
TextoTenis3.place(x=855,y=330)

Tenis4 = PhotoImage(file="icons/Tenis4.png")
LogoLabel1 = Label(Frame, image=Tenis4, bg="white")
LogoLabel1.place(x=300, y=450)
TextoTenis4 = Label(Frame,text="Exemplo Tenis 4",font = "Arial",bg="White")
TextoTenis4.place(x=335,y=600)
TextoTenis4 = Label(Frame,text="R$:700,00",font = "Arial",bg="White")
TextoTenis4.place(x=355,y=630)

Tenis5 = PhotoImage(file="icons/Tenis5.png")
LogoLabel1 = Label(Frame, image=Tenis5, bg="white")
LogoLabel1.place(x=550, y=450)
TextoTenis5 = Label(Frame,text="Exemplo Tenis 5",font = "Arial" ,bg="White")
TextoTenis5.place(x=585,y=600)
TextoTenis5 = Label(Frame,text="R$:134,00",font = "Arial",bg="White")
TextoTenis5.place(x=605,y=630)

Tenis6 = PhotoImage(file="icons/Tenis6.png")
LogoLabel1 = Label(Frame, image=Tenis6, bg="white")
LogoLabel1.place(x=800, y=450)
TextoTenis6 = Label(Frame,text="Exemplo Tenis 6",font = "Arial",bg="White")
TextoTenis6.place(x=835,y=600)
TextoTenis6 = Label(Frame,text="R$:240,00",font = "Arial",bg="White")
TextoTenis6.place(x=855,y=630)



Modelo = Label(Frame,text="Modelo",font = "Arial", bg="lightblue")
Modelo.place(x=100,y=200)
setaa = PhotoImage(file="icons/setaa.png")
SetaModelo = Label(Frame, image=setaa, bg= "lightblue")
SetaModelo.place(x=80, y=195)

Categoria = Label(Frame,text="Categoria",font = "Arial", bg="lightblue")
Categoria.place(x=100,y=230)
setaa2 = PhotoImage(file="icons/setaa.png")
SetaCategoria = Label(Frame, image=setaa2, bg= "lightblue")
SetaCategoria.place(x=80, y=225)

Preço = Label(Frame,text="Preço",font = "Arial", bg="lightblue")
Preço.place(x=100,y=260)
setaa3= PhotoImage(file="icons/setaa.png")
SetaPreço = Label(Frame, image=setaa3, bg= "lightblue")
SetaPreço.place(x=80, y=255)

Cor = Label(Frame,text="Cor",font = "Arial", bg="lightblue")
Cor.place(x=100,y=290)
setaa4= PhotoImage(file="icons/setaa.png")
SetaCor = Label(Frame, image=setaa4, bg= "lightblue")
SetaCor.place(x=80, y=285)

Tamanho = Label(Frame,text="Tamanho",font = "Arial", bg="lightblue")
Tamanho.place(x=100,y=320)
setaa5= PhotoImage(file="icons/setaa.png")
SetaTamanho = Label(Frame, image=setaa5, bg= "lightblue")
SetaTamanho.place(x=80, y=315)



jan.mainloop()