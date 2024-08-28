from Banco import Banco

class Cidades(object):
    def __init__(self, idcidade=0, cidade="", uf=""):
        self.info = {}
        self.idcidade = idcidade
        self.cidade = cidade
        self.uf= uf

    def insertCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO tbl_cidades (cidade, uf) VALUES (?, ?)",
                      (self.cidade, self.uf))
            banco.conexao.commit()
            c.close()
            return "Cidade cadastrada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção da cidade: {e}"

    def updateCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE tbl_cidades SET cidade = ?, uf = ? WHERE idcidade = ?",
                      (self.cidade, self.uf, self.idcidade))
            banco.conexao.commit()
            c.close()
            return "Cidade atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do cidade: {e}"

    def deleteCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM tbl_cidades WHERE idcidade = ?", (self.idcidade,))
            banco.conexao.commit()
            c.close()
            return "Cidade excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do cidade: {e}"

    def selectCidade(self, idcidade):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidades WHERE idcidade = ?", (idcidade,))
            linha = c.fetchone()
            if linha:
                self.idcidade = linha[0]
                self.cidade = linha[1]
                self.uf = linha[2]

                c.close()
                return "Busca feita com sucesso!"
            else:
                c.close()
                return "Cidade não encontrado."
        except Exception as e:
            return f"Ocorreu um erro na busca do cidade: {e}"
