# A radiobutton lets you choose among a number of mutually exclusive options. 
# Radiobuttons are used together in a set and are appropriate when the number of 
# choices is fairly small (about 3-5). A Radiobutton object has these attributes: 
#     • parent- the parent object 
#     • text- the text label to display 
#     • command- the callback function 
#     • variable- the variable shared among radiobuttons of a set 
#     • value- the speciﬁc value of the radiobutton

import tkinter as tk

root = tk.Tk()
var = tk.StringVar()
var.set('English')
# def cb():
#     print(var.get())

# tk.Radiobutton(root, text='English', variable=var, value='English', command=cb).pack()
# tk.Radiobutton(root, text='German', variable=var, value='German', command=cb).pack()
# tk.Radiobutton(root, text='French', variable=var, value='French', command=cb).pack()

items = {"Q1.": 
                {"question": "What language are you speaking ?",
                 "options": ['English', 'German', "French", "Italian", "Spanish"],
                 "answer": "English",
                },
        "Q2.": 
                {"question": "What stack are you learning ?",
                 "options": ['frontend', 'backend', "full-stack", "ui/ux", "product-management"],
                 "answer": "backend"
                },
        "Q3.": 
                {"question": "What python leel are you ?",
                 "options": ['beginner', 'intermediate', "adance", "expert", "senior-expert"],
                 "answer": "adance",
                },
        "Q4.": 
                {"question": "What is your job status ?",
                 "options": ['employed', 'unemployed', "self-employed", "working", "trading"],
                 "answer": "self-employed"
                },
        "Q5.": 
                {"question": "What is your prefered food ?",
                 "options": ['rice', 'beans', "plantain", "yam", "fruit"],
                 "answer": "beans",
                }

            }
var = tk.StringVar()
key = "Q"

def cb():
    print(var.get())


for i, x in enumerate(items.items()):
    # print(x['question'])
    # print(x['options'])
    print(x)
    lb_y_pos = 20
    lt = tk.Label(root, text=x, bg='black', fg='white')
    lt.place(x=20, y=lb_y_pos)
    lb_y_pos +=100
    r_y_pos = 25
    count = 0
    while count <= 5:
        r = tk.Radiobutton(root, text=x[i], 
        variable=var, value=x, command=cb)
        r.place(x=50, y=r_y_pos)
    r_y_pos += 5

root.mainloop()
