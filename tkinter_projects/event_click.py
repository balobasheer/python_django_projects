import tkinter as tk

parent = tk.Tk()
label = tk.Label(parent, text='starting...', font='Arial 36')
label.pack()
label.bind('<Enter>', lambda e: label.configure(text='mouse inside'))
label.bind('<Leave>', lambda e: label.configure(text='mouse outside'))
label.bind('<1>', lambda e: label.configure(text='mouse click'))

parent.mainloop()