import mysql.connector

class Database:
    def __init__(self, banco = "perkal") -> None:
        self.banco = banco

    def connect(self):
        print("=" * 50)
        self.conn = mysql.connector.connect(host='127.0.0.1',database=self.banco,user='root',password='')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Connectado Com Sucesso")
            print("=" * 50)
        else:
            print("Erro de Conexao")

    def insert(self,tupla):
        print("=" * 50)
        self.connect()
        try:
            self.cursor.execute('INSERT INTO cliente (nome,cpf,fone,cidade) VALUES (%s,%s,%s,%s)', tupla)
            self.conn.commit()
            return True

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()

    def select(self,tabela):
        print("=" * 50)
        self.connect()
        try:
            print("=" * 50)
            self.cursor.execute(f"SELECT * FROM {tabela}")
            result = self.cursor.fetchall()
            for i in result:
                print(i)
            print("=" * 50)
            return f"Tabela {tabela}"

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()    


    def select_by_id(self,tabela, id_cli):
        print("=" * 50)
        self.connect()
        try:
            print("=" * 50)
            self.cursor.execute(f"SELECT * FROM {tabela} WHERE id_cli = {id_cli}")
            result = self.cursor.fetchone()
            return result
            print("=" * 50)

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()    


    def update(self,tabela,id,dado_para_atualizar,dado_atualizado):
        print("=" * 50)
        self.connect()
        try:
            self.cursor.execute(f"UPDATE {tabela} SET {dado_para_atualizar} = '{dado_atualizado}' WHERE id_cli = {id}")
            self.conn.commit()
            return True

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()


    def delete(self,id_cli):
        print("=" * 50)
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM cliente WHERE id_cli = {id_cli}")
            self.conn.commit()
            return True
            print("=" * 50)

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexao encerrada com Sucesso!!!")
            print("=" * 50)



db = Database()

# db.connect()

# dados = ("Ederson","333","313","RJ")
# cadastro = db.insert(dados)
# if cadastro == True:
#     print("Cadastrado com Sucesso")

# deletar = db.delete(12)
# if deletar == True:
#     print("Deletado com Sucesso")

# print(db.select("cliente"))
# print(db.select_by_id("cliente",10))

# print(db.update("cliente",16,"nome","Joao Pedro"))

# atualizar = db.update("cliente",9,"nome","Proj JOW-JOW")
# if atualizar:
#     print("Dado atualizado com Sucesso")