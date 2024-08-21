import itertools
import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
style_1 = {'fg': 'red', 'bg': 'black', 'activebackground': 'gold', 'activeforeground': 'dim gray'}
style_2 = {'fg': 'yellow', 'bg': 'grey', 'activebackground': 'chocolate', 'activeforeground': 'blue4'}
style_cycle = itertools.cycle([style_1, style_2])

def switch_style():
    style = next(style_cycle)
    button.configure(**style)
# win = tk.Tk()
button = tk.Button(window, text="style switch", command=switch_style)
button.pack(padx=50, pady=50)

window.mainloop()