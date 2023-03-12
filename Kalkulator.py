import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Kalkulator Hasbi")
        master.config(bg='#EDF1D6')

        # Membuat Tampilan Widget 
        self.display = tk.Entry(master, bg='#9DC08B', width=30, justify="right")
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

        # Pembuatan Tombol (Button)
        button_colors = {
            "1": "#FFDEAD", "2": "#FFDEAD", "3": "#FFDEAD", "/": "#B3E5BE", "C": "#B22222",
            "4": "#FFDEAD", "5": "#FFDEAD", "6": "#FFDEAD", "*": "#B3E5BE", "Del": "#B22222",
            "7": "#FFDEAD", "8": "#FFDEAD", "9": "#FFDEAD", "-": "#B3E5BE", "Exit": "#B22222",
            "0": "#FFDEAD", ".": "#B3E5BE", "=": "#B3E5BE", "+": "#B3E5BE", 
        }
        buttons = [
            "1", "2", "3", "/", "C",
            "4", "5", "6", "*", "Del",
            "7", "8", "9", "-", "Exit",
            "0", ".", "=", "+", 
        ]

        # Menambahkan Tombol (Button) ke tampilan
        row = 1
        col = 0
        for button in buttons:
            if button == "":
                continue
            command = lambda x=button: self.button_click(x)
            tk.Button(master, text=button, width=5, bg=button_colors[button],  font=("Helvetica", 16), command=command).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Configure the grid to resize with the window
        for i in range(5):
            master.grid_columnconfigure(i, weight=1)
        for i in range(6):
            master.grid_rowconfigure(i, weight=1)

    def button_click(self, button):
        if button == "C":
            self.display.delete(0, tk.END)
        elif button == "CE":
            self.display.delete(0, tk.END)
        elif button == "Exit":
            self.master.destroy()
        elif button == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif button == "Del":
            self.display.delete(len(self.display.get())-1, tk.END)
        else:
            self.display.insert(tk.END, button)

# Create the main window and start the event loop
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
calculator = Calculator(root)
root.mainloop()