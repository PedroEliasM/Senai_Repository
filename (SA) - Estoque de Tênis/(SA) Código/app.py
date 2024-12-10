import os
from tkinter import *
from tkinter import font
import tkinter as tk
from tkinter.ttk import Style
from tkinter import messagebox

from Usuarios import Usuarios

import mysql.connector
# pip install mysql-connector-python
# pip install typing-extensions
# O "typing-extensions" é para o caso de usar "self"

HOST = "localhost"
USER = "root"
PASSWORD = "root"
DATABASE = "loja_de_tenis"

def tela_cadastro():
    frame2.place_forget()
    frame1.place(width=500, height=400)

    lbl_nome = Label(frame1, text="Nome:")
    lbl_nome.place(x=100, y=100)
    txt_nome = Entry(frame1, width=30)
    txt_nome.place(x=160, y=102)

    lbl_email = Label(frame1, text="Email:")
    lbl_email.place(x=100, y=130)
    txt_email = Entry(frame1, width=30)
    txt_email.place(x=160, y=132)

    lbl_telefone = Label(frame1, text="Telefone:")
    lbl_telefone.place(x=100, y=160)
    txt_telefone = Entry(frame1, width=30)
    txt_telefone.place(x=160, y=162)

    lbl_endereco = Label(frame1, text="Endereço:")
    lbl_endereco.place(x=100, y=190)
    txt_endereco = Entry(frame1, width=30)
    txt_endereco.place(x=160, y=192)

    lbl_senha = Label(frame1, text="Senha:")
    lbl_senha.place(x=100, y=220)
    txt_senha = Entry(frame1, width=30, show="*")
    txt_senha.place(x=160, y=222)

    def registrar_usuario():
        nome = txt_nome.get()
        email = txt_email.get()
        telefone = txt_telefone.get()
        endereco = txt_endereco.get()
        senha = txt_senha.get()

        # Check if all fields are filled
        if not nome or not email or not telefone or not endereco or not senha:
            messagebox.showerror("Erro! Por favor, preencha todos os campos obrigatórios.")
            return

        try:
            # Connect to the database
            conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
            cursor = conn.cursor()

            # Check if user already exists (using email, telefone, as a unique identifier)
            sql = "SELECT * FROM cliente WHERE email = %s OR telefone = %s"
            val = (email, telefone)
            cursor.execute(sql, val)
            result = cursor.fetchone()

            if result:
                messagebox.showerror("Erro! Já existe um usuário com este email ou telefone.")
                return

            # Insert user data into the database
            sql = "INSERT INTO cliente (nome, email, telefone, endereco, senha) VALUES (%s, %s, %s, %s, %s)"
            val = (nome, email, telefone, endereco, senha)
            cursor.execute(sql, val)
            conn.commit()

            messagebox.showinfo("Cadastro realizado com sucesso!")
            limpar_campos_cadastro()

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {err}")
        finally:
            # Close the database connection (if open)
            if conn:
                conn.close()

    # Add a button to trigger registration
    btn_registrar = Button(frame1, text="Registrar", command=registrar_usuario)
    btn_registrar.place(x=200, y=260)


def tela_login():
    frame1.place_forget()
    frame2.place(width=500, height=400)

    lbl_email_login = Label(frame2, text="Email:")
    lbl_email_login.place(x=100, y=130)
    txt_email_login = Entry(frame2, width=30)
    txt_email_login.place(x=160, y=132)

    lbl_senha_login = Label(frame2, text="Senha:")
    lbl_senha_login.place(x=100, y=160)
    txt_senha_login = Entry(frame2, width=30, show="*")
    txt_senha_login.place(x=160, y=162)

    def verificar_login():
            email = txt_email_login.get()
            senha = txt_senha_login.get()

            admin_email = "adm"
            admin_senha = "123"

            if not email or not senha:
                messagebox.showerror("Erro! Por favor, preencha todos os campos obrigatórios.")
                return

            # Verifica se é o administrador
            if email == admin_email and senha == admin_senha:
                messagebox.showinfo("Sucesso", "Bem-vindo, administrador!")
                frame2.place_forget()
                frame_admin.place(width=500, height=400)
                return  # Encerra a função após o login de administrador

            try:
                conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
                cursor = conn.cursor()

                # Consultar o banco de dados para verificar as credenciais
                sql = "SELECT senha FROM cliente WHERE email = %s"
                val = (email,)
                cursor.execute(sql, val)
                resultado = cursor.fetchone()

                if resultado:
                    senha_armazenada = resultado[0]
                    if senha == senha_armazenada:
                        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
                        frame2.place_forget()
                        frame_usuario.place(width=500, height=400)
                    else:
                        messagebox.showerror("Erro", "Senha incorreta.")
                else:
                    messagebox.showerror("Erro", "Usuário não encontrado.")

            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao verificar login: {err}")
            finally:
                if conn:
                    conn.close()

    # Botão para verificar o login
    btn_login = Button(frame2, text="Login", command=verificar_login)
    btn_login.place(x=200, y=192)


def voltar():
    frame1.place_forget()
    frame2.place_forget()

def limpar_campos_cadastro():  # Function to clear entry fields
    txt_nome.delete(0, tk.END)
    txt_email.delete(0, tk.END)
    txt_telefone.delete(0, tk.END)
    txt_endereco.delete(0, tk.END)
    txt_senha.delete(0, tk.END)


# TELA PRINCIPAL
Janela = Tk()
Janela.geometry("700x400+700+200")
Janela.configure(bg="lightblue")
# ESTRUTURA DA TELA INICIAL
Label(Janela, text="Bem vindo a Loja NIKE", fg="black", font=("Arial", 16, "bold")).pack(pady=20)
Button(text="Fazer Cadastro", command= tela_cadastro).pack()
Button(text="Fazer Login", command= tela_login).pack(pady=10)

# OUTRAS TELAS
frame1 = Frame(Janela, bg="lightblue")
Button(frame1, text="Voltar", command=voltar).pack()

frame2 = Frame(Janela, bg="lightblue")
Button(frame2, text="Voltar", command=voltar).pack()



# ADMIN ------------------------------------------------------------- ADMIN
frame_admin = Frame(Janela, bg="lightblue")
label = Label(frame_admin, text="ADMIN")
label.pack()
        
def criar_produto():
    lbl_modelo = Label(frame_admin, text="Modelo:")
    lbl_modelo.place(x=50, y=100)
    txt_modelo = Entry(frame_admin, width=30)
    txt_modelo.place(x=180, y=102)

    lbl_categoria = Label(frame_admin, text="Categoria:")
    lbl_categoria.place(x=50, y=130)
    txt_categoria = Entry(frame_admin, width=30)
    txt_categoria.place(x=180, y=132)

    lbl_tamanho = Label(frame_admin, text="Tamanho:")
    lbl_tamanho.place(x=50, y=160)
    txt_tamanho = Entry(frame_admin, width=30)
    txt_tamanho.place(x=180, y=162)

    lbl_cor = Label(frame_admin, text="Cor:")
    lbl_cor.place(x=50, y=190)
    txt_cor = Entry(frame_admin, width=30)
    txt_cor.place(x=180, y=192)

    lbl_preco = Label(frame_admin, text="Preço:")
    lbl_preco.place(x=50, y=220)
    txt_preco = Entry(frame_admin, width=30)
    txt_preco.place(x=180, y=222)

    btn_salvar_produto = Button(frame_admin, text="Salvar Produto", command=lambda: salvar_produto(
        txt_modelo.get(), txt_categoria.get(), txt_tamanho.get(), txt_cor.get(), txt_preco.get()
    ))
    btn_salvar_produto.place(x=180, y=282)

def salvar_produto(modelo, categoria, tamanho, cor, preco):

    try:
        conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
        cursor = conn.cursor()

        # Consultar o banco de dados para verificar as credenciais
        sql = "INSERT INTO produto (modelo, categoria, tamanho, cor, preco) VALUES (%s, %s, %s, %s, %s)"
        val = (modelo, categoria, tamanho, cor, preco)
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo("Produto cadastrado com sucesso!")

    finally:
        if conn:
            conn.close()

def editar_produto():
    cursor.execute("UPDATE produto SET modelo=%s, categoria=%s, tamanho=%s, cor=%s, preco=%s WHERE id=%s", ())
    conn.commit()
    messagebox.showinfo("Sucesso", "Produto editado com sucesso!")
    # Fecha a janela de edição
    janela_editar.destroy()

def excluir_produto():
    criar_produto().show = False
    lbl_excluir = Label(frame_admin, text="Excluir")
    lbl_excluir.place(x=50, y=100)
    txt_excluir = Entry(frame_admin, width=30)
    txt_excluir.place(x=180, y=102)
    if messagebox.askyesno("Tem certeza que deseja excluir este produto?"):
        cursor.execute("DELETE FROM produto WHERE id=%s", (id_produto,))
        conn.commit()
        messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")

# Botões para gerenciar produtos
btn_criar_produto = Button(frame_admin, text="Criar Produto", command=criar_produto)
btn_criar_produto.pack()

btn_editar_produto = Button(frame_admin, text="Editar Produto", command=editar_produto)
btn_editar_produto.pack()

btn_excluir_produto = Button(frame_admin, text="Excluir Produto", command=excluir_produto)
btn_excluir_produto.pack()


# USUARIO ------------------------------------------------------------- USUARIO
frame_usuario = Frame(Janela, bg="lightgreen")
label = Label(frame_usuario, text="NIKE")
label.pack()

Janela.mainloop()