import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")

        self.equation = tk.StringVar()
        self.entry_value = ""
        self.create_widgets()

    def create_widgets(self):
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=20)
        
        entry = tk.Entry(entry_frame, textvariable=self.equation, font=('arial', 18), bd=10, insertwidth=2, width=14, borderwidth=4, bg="#ffffff", fg="#000000")
        entry.grid(row=0, column=0)

        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ('7', 1, 0, "#e0e0e0", "#000000"), ('8', 1, 1, "#e0e0e0", "#000000"), ('9', 1, 2, "#e0e0e0", "#000000"), ('/', 1, 3, "#ffcccb", "#000000"),
            ('4', 2, 0, "#e0e0e0", "#000000"), ('5', 2, 1, "#e0e0e0", "#000000"), ('6', 2, 2, "#e0e0e0", "#000000"), ('*', 2, 3, "#ffcccb", "#000000"),
            ('1', 3, 0, "#e0e0e0", "#000000"), ('2', 3, 1, "#e0e0e0", "#000000"), ('3', 3, 2, "#e0e0e0", "#000000"), ('-', 3, 3, "#ffcccb", "#000000"),
            ('0', 4, 0, "#e0e0e0", "#000000"), ('.', 4, 1, "#e0e0e0", "#000000"), ('+', 4, 2, "#ffcccb", "#000000"), ('=', 4, 3, "#90ee90", "#000000"),
            ('C', 5, 0, "#ff0000", "#ffffff", 4)
        ]

        for (text, row, col, bg_color, fg_color, *span) in buttons:
            action = lambda x=text: self.click_event(x)
            button = tk.Button(button_frame, text=text, padx=20, pady=20, font=('arial', 18), command=action, bg=bg_color, fg=fg_color)
            if span:
                button.grid(row=row, column=col, columnspan=span[0])
            else:
                button.grid(row=row, column=col)

    def click_event(self, key):
        if key == "=":
            try:
                result = str(eval(self.entry_value))
                self.equation.set(result)
                self.entry_value = result
            except:
                messagebox.showerror("Error", "Invalid Input")
                self.entry_value = ""
                self.equation.set(self.entry_value)
        elif key == "C":
            self.entry_value = ""
            self.equation.set(self.entry_value)
        else:
            self.entry_value += str(key)
            self.equation.set(self.entry_value)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
