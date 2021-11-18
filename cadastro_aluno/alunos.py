from banco import Banco

class Alunos(object):

    def __init__(self, idaluno = 0, nome = "", endereco = "",
        email = "", periodo = "", campus = ""):
        self.info = {}
        self.idaluno = idaluno
        self.nome = nome
        self.email = email
        self.endereco = endereco
        
        self.periodo = periodo
        self.campus = campus


    def insertUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into alunos (nome, endereco, email,periodo, campus) values ('" + self.nome + "', '" +
            self.endereco + "', '" + self.email + "', '" +
            self.periodo + "', '" + self.campus + "' )")

            banco.conexao.commit()
            c.close()

            return "Aluno cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do aluno"

    def updateUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update alunos set nome = '" + self.nome + "', endereco = '" + self.endereco + "', email = '" + self.email +
            "', periodo = '" + self.periodo + "', campus = '" + self.campus +
            "' where idaluno = " + self.idaluno + " ")

            banco.conexao.commit()
            c.close()

            return "Aluno atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do aluno"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from alunos where idaluno = " + self.idaluno + " ")

            banco.conexao.commit()
            c.close()

            return "Aluno excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do aluno"

    def selectUser(self, idaluno):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from alunos where idaluno = " + idaluno + "  ")

            for linha in c:
                self.idaluno = linha[0]
                self.nome = linha[1]
                self.endereco = linha[2]
                self.email = linha[3]
                self.periodo = linha[4]
                self.campus = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do aluno"

    def selectAllUsers(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from alunos ;")

            todosAlunos = ""

            for linha in c:
                todosAlunos += str(linha[0]) + " - "+linha[1]+"\n"
                todosAlunos += "-"*20 + "\n"
            c.close()

            return todosAlunos  #"Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do aluno"