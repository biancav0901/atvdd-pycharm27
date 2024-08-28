import tkinter as tk
from tkinter import messagebox
from Formulario import Application as UserForm
from Cidade import Cidade as Cidform

class MainMenu:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Sistema de Gestão")

        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=20, pady=20)

        self.title_label = tk.Label(self.frame, text="Menu Principal", font=("Verdana", 16, "bold"))
        self.title_label.pack(pady=10)

        # Botão para acessar a tela de usuários
        self.user_button = tk.Button(self.frame, text="Usuários", width=20, command=self.open_user_screen)
        self.user_button.pack(pady=5)

        # Botão para acessar a tela de cidades
        self.city_button = tk.Button(self.frame, text="Cidades", width=20, command=self.open_city_screen)
        self.city_button.pack(pady=5)

        # Botão para acessar a tela de clientes
        self.client_button = tk.Button(self.frame, text="Clientes", width=20, command=self.open_client_screen)
        self.client_button.pack(pady=5)

        # Botão para sair do sistema
        self.exit_button = tk.Button(self.frame, text="Sair", width=20, command=self.master.quit)
        self.exit_button.pack(pady=5)

    def open_user_screen(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = UserForm(self.new_window)

    def open_city_screen(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Cidform(self.new_window)

    def open_client_screen(self):
        # Aqui você vai implementar a lógica para abrir a tela de clientes
        messagebox.showinfo("Tela de Clientes", "Abrir tela de clientes")

if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")  # Define o estado da janela como maximizada
    app = MainMenu(master=root)
    root.mainloop()
