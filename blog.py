import tkinter as tk
from tkinter import messagebox

class BlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blog de Inteligência Artificial")
        
        self.logged_in = False
        self.username = "usuario"
        self.password = "senha"
        
        self.login_frame = tk.Frame(self.root)
        self.blog_frame = tk.Frame(self.root)
        
        self.create_login_frame()
        self.create_blog_frame()
        
        self.root.geometry("600x400+400+200")  # Inicializa o programa na metade da tela e centralizado
        self.login_frame.pack()
    
    def create_login_frame(self):
        self.label_username = tk.Label(self.login_frame, text="Usuário:")
        self.label_password = tk.Label(self.login_frame, text="Senha:")
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.button_login = tk.Button(self.login_frame, text="Login", command=self.check_login)
        
        self.label_username.pack()
        self.entry_username.pack()
        self.label_password.pack()
        self.entry_password.pack()
        self.button_login.pack()
    
    def check_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if username == self.username and password == self.password:
            self.logged_in = True
            self.login_frame.pack_forget()
            self.blog_frame.pack()
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos.")
    
    def create_blog_frame(self):
        self.label_heading = tk.Label(self.blog_frame, text="Bem-vindo ao Blog de IA")
        
        self.label_heading.pack()
        
        self.sample_blogs = [
            "Notícia 1: Avanços recentes na IA",
            "Notícia 2: Ética na Inteligência Artificial",
            "Notícia 3: Aplicações práticas de IA na indústria"
        ]
        
        self.blog_entries = []
        
        self.update_blog_frame()
        
        self.entry_new_blog = tk.Entry(self.blog_frame, width=50)
        self.button_add_blog = tk.Button(self.blog_frame, text="Adicionar Blog", command=self.add_blog)
        
        self.entry_new_blog.pack()
        self.button_add_blog.pack()
    
    def update_blog_frame(self):
        for entry in self.blog_entries:
            entry.destroy()
        
        self.blog_entries = []
        
        for blog in self.sample_blogs:
            label_blog = tk.Label(self.blog_frame, text=blog)
            self.blog_entries.append(label_blog)
            label_blog.pack()
    
    def add_blog(self):
        new_blog = self.entry_new_blog.get()
        if new_blog:
            self.sample_blogs.append(new_blog)
            self.entry_new_blog.delete(0, tk.END)
            self.update_blog_frame()

if __name__ == "__main__":
    root = tk.Tk()
    app = BlogApp(root)
    root.mainloop()
