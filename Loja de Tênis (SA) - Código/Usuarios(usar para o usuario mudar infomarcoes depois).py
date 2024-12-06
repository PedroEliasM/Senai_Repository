import mysql.connector
from Database import Database

class Usuarios(object):
    def __init__(self, cd_cliente=0, nome="", email="", telefone="", endereco="", senha=""):
        self.info = {}
        self.cd_cliente = cd_cliente
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.senha = senha

    def insertUser(self):
        database = Database()
        try:
            c = database.conexao.cursor()
            c.execute("INSERT INTO cliente(nome, email, telefone, endereco, senha) VALUES(%s,%s,%s,%s,%s)",
                            (self.nome,self.email,self.telefone,self.endereco,self.senha))
            database.conexao.commit()
            c.close()
            return "Usuario cadastrado com sucesso!"

        except Exception as e:
            return f"Ocorreu um erro na inserção de usuário: {e}"

    def updateUser(self):
        database = Database()
        try:
            c = database.conexao.cursor()
            c.execute("UPDATE cliente SET nome = %s, email = %s, telefone = %s, endereco = %s, senha = %s WHERE cd_cliente = %s",
                            (self.nome,self.email,self.telefone,self.endereco,self.senha))
            database.conexao.commit()
            c.close()
            return "Usuario alterado com sucesso!"
            
        except Exception as e:
            return f"Ocorreu um erro na alteração de usuário: {e}"

