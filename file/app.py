import tkinter as tk
class App (tk.Frame):
    # Construtor da Sub Classe
    def __init__ (self):
        self.msg: tk.Label
        self.botaoBuscar: tk.Button
        self.msgResultado: tk.Label
        self.botaoSair: tk.Button
        # Construtor da Super Classe
        tk.Frame.__init__(self)
        print("Olá")
        self.desenharTela()
    
    def desenharTela(self):
        self.master.geometry("600x620")
        self.msg = tk.Label(self.master, text= "Informat nome do Arquivo.")
        self.msg.pack()

        self.butaoBuscar = tk.Button(self.master)
        self.butaoBuscar["text"] = "Clique buscar"
        self.butaoBuscar["font"] = ("Calibri", "12")
        self.butaoBuscar["width"] = 30
        self.butaoBuscar["command"] = self.buscarArquivo
        self.butaoBuscar.pack()

        self.msgResultado = tk.Label(self.master, text="Resultado após clicar.")
        
        self.botaoSair = tk.Button(self.master, text="Sair" , bg="red", fg="white", width="20", command= self.quit)
        self.botaoSair.pack()

    def buscarArquivo(self):
        print("Olá, sou o Buscar Arquivo.")

obj = App()
obj.mainloop()