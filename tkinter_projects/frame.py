import tkinter as tk

root = tk.Tk()

# • padding - extra space inside the frame 
# • borderwidth 
# • relief (ﬂat, raised, sunken, solid, ridge, grove) 
# • width 
# • heigh

for x in ('flat', 'raised', 'sunken', 'solid', 'ridge', 'groove'):
    frame = tk.Frame(root, relief=x, borderwidth=5, background='red')
    frame.pack(side='left')
    tk.Label(frame, text=x).pack()
root.mainloop()