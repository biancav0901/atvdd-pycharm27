from tkinter import END, INSERT


class YourClassName:
    def _init_(self):
        # Assume that you have initialized your widgets here
        self.btnBuscar["command"] = self.buscarUsuario
        self.bntInsert["command"] = self.inserirUsuario
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntExcluir["command"] = self.excluirUsuario

    def buscarusuario(self):
        user = usuarios()  # Initialize usuarios object
        idusuario = self.txtidusuario.get()
        user_info = user.selectUser(idusuario)  # Retrieve user info

        # Check if user_info is valid before updating the fields
        if user_info:
            self.lblmsg["text"] = "usuário encontrado."
            self.txtidusuario.delete(0, END)
            self.txtidusuario.insert(INSERT, user_info.idusuario)
            self.txtnome.delete(0, END)
            self.txtnome.insert(INSERT, user_info.nome)
            self.txttelefone.delete(0, END)
            self.txttelefone.insert(INSERT, user_info.telefone)
            self.txtemail.delete(0, END)
            self.txtemail.insert(INSERT, user_info.email)
            self.txtusuario.delete(0, END)
            self.txtusuario.insert(INSERT, user_info.usuario)
            self.txtsenha.delete(0, END)
            self.txtsenha.insert(INSERT, user_info.senha)
        else:
            self.lblmsg["text"] = "usuário não encontrado."

    def inserirusuario(self):
        user = Usuarios()  # Initialize usuarios object
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        # Check if insertUser returns a success or failure message
        self.lblmsg["text"] = user.insertUser()
        self.limparCampos()

    def alterarusuario(self):
        user = Usuarios()  # Initialize Usuarios object
        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        # Check if updateUser returns a success or failure message
        self.lblmsg["text"] = user.updateUser()
        self.limparCampos()

    def excluirusuario(self):
        user = usuarios()  # Initialize Usuarios object
        user.idusuario = self.txtidusuario.get()

        # Check if deleteUser returns a success or failure message
        self.lblmsg["text"] = user.deleteUser()
        self.limparCampos()

    def limparCampos(self):
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)