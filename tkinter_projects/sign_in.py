import tkinter as tk
import tkinter.messagebox as msgbox


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Name is ")

        self.label_text = tk.StringVar()
        self.label_text.set("Choose One")

        self.name_text = tk.StringVar()

        self.label = tk.Label(
            self, text=self.label_text.get(), 
            textvariable=self.label_text
            )
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=30)

        self.name_entry = tk.Entry(self, textvariable=self.name_text)
        self.name_entry.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)

        hello_button = tk.Button(self, text="Say Hello",command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))

        goodbye_button = tk.Button(self, text="Say Goodbye",command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

    def say_hello(self):
        message = "Hello there " + self.name_entry.get()
        msgbox.showinfo("Hello", message)

    # def say_goodbye(self):
    #     self.label_text.set("Goodbye! \n (Closing in 2 seconds)")
    #     msgbox.showinfo("Goodbye", "Goodbye, it is been fun")
    #     self.after(2000, self.destroy)

    def say_goodbye(self):
        if msgbox.askyesno("Close Window?", "Would you like to close this window?"):
            message = "Window will close in 2 seconds - goodybye " + self.name_text.get()
            self.label_text.set(message)
            self.after(2000, self.destroy)
        else:
            msgbox.showinfo("Not Closing", "Great! This window will stay open")
'''
StringVar: This holds characters like a Python string. 
IntVar: This holds an integer value. 
DoubleVar: This holds a double value (a number with a decimal place). 
BooleanVar: This holds a Boolean to act like a flag.
'''

if __name__ == "__main__":
    window = Window()
    window.mainloop()