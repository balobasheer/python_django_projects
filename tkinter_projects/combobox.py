# A combobox combines an entry widget with a list of choices.
# The user can either select text from a drop-down menu or write his own text.
# The Combobox class has the options
#     • parent- for the parent object
#     • textvariable- for the variable which stores the value
#     • values- for the items list
#     • state- to indicate readonly

import tkinter as tk
from tkinter.ttk import ttk
app = App('Combo')
root = tk.Tk()
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
day = tk.StringVar()
day.set(days[0])
ttk.Combobox(App.stack[-1], textvariable=day, values=days).grid()
password = tk.StringVar()
tk.Label(text='Password').pack()
tk.Entry(root, textvariable=password, show='*').pack()
def get_v():
    print(name.get() + " "+ password.get())
tk.Button(root, text='press', command=get_v).pack()

root.mainloop()


