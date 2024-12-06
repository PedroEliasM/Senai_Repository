import mysql.connector

class Database():
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "loja_de_tenis"
        )
        self.create.Table()
        
    def createTable(self):
        c = self.conexao.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS
        usuario(
            cd_cliente INT AUTO_INCREMENT PRIMARY KEY,
            nome varchar(45) not null,
            email varchar(45) not null,
            telefone varchar(20) not null,
            endereco varchar(100) not null,
            senha varchar(20) not null)''')

        self.conexao.commit()
        c.close()