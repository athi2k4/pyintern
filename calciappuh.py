import tkinter as tk
#making a cakciapp
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")

        self.expression = ""

        # Create a text entry box
        self.display = tk.Entry(self.window, font=("Arial", 18), borderwidth=2, relief='solid')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            if button == "=":
                tk.Button(self.window, text=button, font=("Arial", 18), command=self.calculate).grid(row=row, column=col, columnspan=2, padx=5, pady=5, sticky='nsew')
                col += 2
            else:
                tk.Button(self.window, text=button, font=("Arial", 18), command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                col += 1
            if col > 3:
                col = 0
                row += 1

        # Create clear button
        tk.Button(self.window, text='C', font=("Arial", 18), command=self.clear).grid(row=row, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        # Configure grid weights to make buttons resize with window
        for i in range(5):
            self.window.grid_rowconfigure(i, weight=1)
            self.window.grid_columnconfigure(i, weight=1)

        # Bind key events
        self.window.bind("<Key>", self.on_key_press)

        self.window.mainloop()

    def on_button_click(self, char):
        self.expression += str(char)
        self.update_display()

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
        except Exception:
            self.expression = "error"
        self.update_display()

    def clear(self):
        self.expression = ""
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def on_key_press(self, event):
        if event.char in '0123456789+-*/.':
            self.on_button_click(event.char)
        elif event.keysym == "Return":
            self.calculate()
        elif event.keysym == 'Escape':
            self.clear()

if __name__ == '__main__':
    Calculator()
