import tkinter as tk

root = tk.Tk()
main_frame = tk.Frame(root, border=3, relief='groove')
root.geometry(newGeometry="550x550")

for i in range(3):
    tk.Label(main_frame, text="AAAAAAAAAAAA", border=1, relief="groove",
             padx=20, pady=20).grid(column=0, row=i)
root.mainloop()
