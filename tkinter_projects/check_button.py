# A checkbutton is like a regular button, with a label and a callback function, 
# but it also holds and displays a binary state. The Checkbutton object has 
# the following attributes: 
#     • parent- the parent object 
#     • text- the label to display 
#     • command- the callback function 
#     • variable- the variable holding the state value 
#     • onvalue- the value when in the ON state 
#     • offvalue- the value when in the OFF state

import tkinter as tk
root = tk.Tk()
texts = ['English', 'German', 'French']
vars = [tk.StringVar(value='0'), tk.StringVar(value='0'),tk.StringVar(value='0')]
def cb():
    print('--- languages ---')
    for i, s in enumerate(texts):
        print(s, vars[i].get())
tk.Checkbutton(root, text=texts[0], variable=vars[0], command=cb).pack()
tk.Checkbutton(root, text=texts[1], variable=vars[1], command=cb).pack()
tk.Checkbutton(root, text=texts[2], variable=vars[2], command=cb).pack()
root.mainloop()