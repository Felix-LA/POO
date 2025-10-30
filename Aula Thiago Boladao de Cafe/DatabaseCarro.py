import mysql.connector

class DatabaseCarro:
    def __init__(self, banco = "perkal") -> None:
        self.banco = banco
        self.host = "localhost"
        self.user = "root"
        self.password = ""

    def connect(self):
        print("=" * 50)
        self.conn = mysql.connector.connect(host=self.host,database=self.banco,user=self.user,password=self.password)
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Connectado Com Sucesso", db_info)
            print("=" * 50)
        else:
            print("Erro de Conexao")

    def insert(self,tupla):
        print("=" * 50)
        print(tupla)
        self.connect()
        try:
            self.cursor.execute('INSERT INTO carro (modelo,descricao,anoDeFabricacao,valor,motor,dono,numeroDePortas,placa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', tupla)
            self.conn.commit()
            return f"Carro Cadastrado com Sucesso: {tupla}"
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

    def selectByID(self,tabela,id_carro):
        print("=" * 50)
        self.connect()
        try:
            print("=" * 50)
            self.cursor.execute(f"SELECT * FROM {tabela} WHERE id_carro {id_carro}")
            result = self.cursor.fetchone()
            return result

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()    

    def update(self,tabela,id,tupla):
        print("=" * 50)
        self.connect()
        try:
            self.cursor.execute(f"""UPDATE {tabela} SET 
                                modelo = {tupla[1]},descricao = {tupla[2]},anoDeFabricacao = {tupla[3]},valor = {tupla[4]},
                                motor = {tupla[5]},dono = {tupla[6]},numeroDePortas = {tupla[7]},placa = {tupla[8]}
                                WHERE id_carro = {id}""")
            self.conn.commit()
            return True
        
        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()

    def delete(self,id):
        print("=" * 50)
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM carro WHERE id_carro = {id}")
            self.conn.commit()
            return True
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
        

carro = DatabaseCarro()

# carro.connect()

# dados = ("Ferrari","Um carro","2000","100.000","3.0","3","2","1111111")

# cadastro = carro.insert(dados)
# if cadastro == True:
#     print(cadastro)

# carro.select("carro") 
# carro.delete(5)