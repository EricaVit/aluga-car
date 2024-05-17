import customtkinter as ctk
from tkinter import ttk

class ExibirVeiculos(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Visualização de Veículos")
        self.geometry("800x600")
        self.resizable(False,False)

        self.frameTitulo = ctk.CTkFrame(self, width=800, height=100, corner_radius=0)
        self.frameTitulo.pack(fill= 'both', expand=False)
        self.frameTitulo.pack_propagate(False)

        self.frameTabela = ctk.CTkFrame(self, width=800, height=500, corner_radius=0)
        self.frameTabela.pack(fill='both', expand=False)
        self.frameTabela.pack_propagate(False)

        self.labelTitulo = ctk.CTkLabel(self.frameTitulo, text='Visualizar Veículos', font=('Open Sans', 26, 'bold'), text_color='white')
        self.labelTitulo.pack(side='bottom')

        self.tableCarros = ttk.Treeview(self.frameTabela, columns=('Placa', 'Modelo', 'Ano', 'Disponibilidade'))

        self.tableCarros.heading('#0', text='#')
        self.tableCarros.heading('#1', text='Placa')
        self.tableCarros.heading('#2', text='Modelo')
        self.tableCarros.heading('#3', text='Ano')
        self.tableCarros.heading('#4', text='Disponibilidade')

        
        self.tableCarros.column('#0', width=0, stretch=False)
        self.tableCarros.column('#1', width=100, anchor='center')
        self.tableCarros.column('#2', width=200, anchor='center')
        self.tableCarros.column('#3', width=100, anchor='center')
        self.tableCarros.column('#4', width=200, anchor='center')
        
        self.tableCarros.pack(fill='both', expand=False, padx=10, pady=15)

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Treeview', rowheight=40, font=('Open Sans', 12), foreground='white', background="#2b2b2b")
        self.style.configure('Treeview.Heading', font=('Open Sans', 12), foreground='white', background='#2b2b2b')
        self.style.map('Treeview', background=[('selected', '#144870')])


        self.label_exemplo = ctk.CTkLabel(self, text='Janela Visualizar')
        self.label_exemplo.pack()