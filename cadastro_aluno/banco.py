import sqlite3

class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('bancoTrabalhoAV2.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists alunos (
                    idaluno integer primary key autoincrement ,
                    nome text,
                    endereco text,
                    email text,
                    periodo text,
                    campus text)""")
        self.conexao.commit()
        c.close()