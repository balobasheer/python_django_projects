# Several widgets allow to enter text or numerical information in a single ﬁeld.
#     • theEntrywidgets allows to type text
#     • theComboboxallows to either type text or select text from a drop-down list
#     • theSpinboxallows to select from a numerical range or from a list
#     • theScaleallows to use a slider to choose a value

# Entry widget
# An entry widget presents the user an empty ﬁeld where he can enter a text value.
# Each ttk.Entry object has these options:
#     • parent- the parent object
#     • textvariable- the text variable to hold the entered string
#     • width- the numbers of characters
#     • show- to indicate * for passwords 

import tkinter as tk
root = tk.Tk()
name = tk.StringVar()
tk.Label(text='Name').pack()
tk.Entry(root, textvariable=name, width=10).pack()
password = tk.StringVar()
tk.Label(text='Password').pack()
tk.Entry(root, textvariable=password, show='*').pack()
def get_v():
    print(name.get() + " "+ password.get())
tk.Button(root, text='press', command=get_v).pack()

root.mainloop()
