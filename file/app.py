import tkinter as tk
class App (tk.Frame):
    # Construtor da Sub Classe
    def __init__ (self):
        # Construtor da Super Classe
        tk.Frame.__init__(self)
        print("Olá")
        self.desenharTela()
    
    def desenharTela(self):
        self.master.geometry("600x620")
        self.msg = tk.Label(self.master, text= "Informat nome do Arquivo.")
        self.msg.pack()

obj = App()
obj.mainloop()