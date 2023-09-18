import tkinter as tk
from tkinter.filedialog import askopenfilename
import csv
class CalcularMedia(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
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
        self.msgResultado.pack()
        
        self.botaoSair = tk.Button(self.master, text="Sair" , bg="red", fg="white", width="20", command= self.quit)
        self.botaoSair.pack()

    def buscarArquivo(self):
        nomeArquivo = askopenfilename()
        self.msgResultado["text"] = f"Aberto: {nomeArquivo}"
        self.lerArquivoCSV(nomeArquivo)

    def lerArquivoCSV(self, nomeArquivo):
        with open(nomeArquivo, newline='') as csvfile:
            reader = csv.reader(csvfile)

            next(reader)

            for row in reader:
                nome = row[0]
                nota1 = float(row[1])
                nota2 = float(row[2])
                nota3 = float(row[3])

                media = (nota1 + nota2 + nota3) / 3
                mediaFormatada = "{:.2f}".format(media)
                print(f"Nome: {nome} \nMedia: {mediaFormatada}")

                resultado_label = tk.Label(self.master, text=f"Nome: {nome}\nMedia: {mediaFormatada}")
                resultado_label.pack()

obj = CalcularMedia()
obj.mainloop()