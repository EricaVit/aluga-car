import customtkinter as ctk

class ExibirVeiculos(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Visualização de Veículos")
        self.geometry("800x600")
        self.resizable(False,False)

        self.label_exemplo = ctk.CTkLabel(self, text='Janela Visualizar')
        self.label_exemplo.pack()