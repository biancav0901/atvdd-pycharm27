from banco import Banco
class Cidades(object):
    def _init_(self, idcidades = 0, nome = "", telefone = "",
        email = "", cidades = "", senha = ""):
        self.info = {}
        self.idcidades = idcidades
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cidades = cidades
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into tbl_usuarios (nome, telefone, email, usuario, senha) values ('" + self.nome + "', '" + self.telefone + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "' )")
            banco.conexao.commit()
            c.close()
            return "Cidade cadastrada com sucesso!"
        except:
            return "Ocorreu um erro na inserção da cidade"

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update tbl_cidades set nome = '" + self.nome + "',telefone = '" + self.telefone + "', email = '" + self.email +
            "', cidades = '" + self.cidades + "', senha = '" + self.senha +
            "' where idcidades = " + self.idcidades + " ")
            banco.conexao.commit()
            c.close()
            return "Cidade atualizada com sucesso!"
        except:
            return "Ocorreu um erro na alteração da cidade"

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from tbl_usuarios where idcidades = " + self.idcidades + " ")
            banco.conexao.commit()
            c.close()
            return "cidade excluída com sucesso!"
        except:
            return "Ocorreu um erro na exclusão da cidade"

    def selectUser(self, idcidades):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from tbl_usuarios where idcidades = " + idcidades + " ")
            for linha in c:
                self.idcidades = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca da cidade"