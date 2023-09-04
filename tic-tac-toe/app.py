import tkinter as tk

root = tk.Tk()
root.geometry("550x550")

main_frame = tk.Frame(root, border=3, relief='groove')
main_frame.pack(expand=True, fill="both")  # Usando pack para expandir e preencher

for i in range(3):
    for j in range(3):
        tk.Label(main_frame, text="A", border=1, relief="groove",
                 padx=20, pady=20).grid(row=i, column=j)

root.mainloop()