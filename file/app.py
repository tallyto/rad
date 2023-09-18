import tkinter as tk
class App (tk.Frame):
    # Construtor da Sub Classe
    def __init__ (self):
        # Construtor da Super Classe
        tk.Frame.__init__(self)
        print("Olá")

obj = App()
obj.mainloop()