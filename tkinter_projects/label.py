import tkinter as tk
root = tk.Tk()
# fonts = ['Times', 'Courier', 'Helvetica', 'Didot']
str_ = tk.StringVar(value='dynamic text')
print(str_.get())
tk.Label(root, text='static text', background='green').pack()
tk.Label(root, textvariable=str_).pack()
tk.Label(root, text='both', textvariable=str_).pack()
tk.Label(root, text='Arial 24', font='Arial 24').pack()
tk.Label(root, text='foreground=red', foreground='red').pack()

c = tk.Canvas(width=12, background='green', height=12)
c.create_line(10,10, 200,200, fill='red')
root.mainloop()