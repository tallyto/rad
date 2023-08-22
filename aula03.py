import tkinter as tk

def exit_button(master: tk.Tk):
    windows_width = 300
    windows_heigth = 200
    screen_width = root.winfo_screenwidth()
    screen_heigth = root.winfo_screenheight()
    center_x = int(screen_width/2 - windows_heigth/2)
    center_y = int(screen_heigth/2 - windows_heigth/2)
    master.geometry(f'{windows_width}x{windows_heigth}+{center_x}+{center_y}')
    master.resizable(False, False)
    button = tk.Button(master, text="Sair",bg="red",fg="white",command=master.quit)
    button.pack()


root = tk.Tk()
root.title("Usando tkinter")
exit_button(root)
root.mainloop()