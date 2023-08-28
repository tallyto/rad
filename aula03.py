import tkinter as tk

def center_window(window):
    window_width = 300
    window_height = 200
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    window.resizable(False, False)

def exit_button(master):
    button = tk.Button(master, text="Sair", bg="red", fg="white", command=master.quit)
    button.pack()

root = tk.Tk()
root.title("Usando tkinter")
center_window(root)
exit_button(root)
root.mainloop()
