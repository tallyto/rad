import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.msg = tk.Label(self, text="Hello World")
        self.msg.pack()
        self.bye = tk.Button(self, text="Bye", command=self.quit)
        self.bye.pack()
        self.pack()

app = Application()
app.mainloop()