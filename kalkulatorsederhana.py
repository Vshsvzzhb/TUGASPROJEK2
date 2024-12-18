import tkinter as tk
from tkinter import ttk

def calculate(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def append_text(text):
    entry.insert(tk.END, text)


root = tk.Tk()
root.title("Kalkulator Sederhana")


entry = ttk.Entry(root, font=('Arial', 20), justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        btn = ttk.Button(root, text=button, command=calculate)
        btn.grid(row=row_val, column=col_val, sticky='nsew')
    else:
        btn = ttk.Button(root, text=button, command=lambda t=button: append_text(t))
        btn.grid(row=row_val, column=col_val, sticky='nsew')
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


btn_clear = ttk.Button(root, text='C', command=lambda: entry.delete(0, tk.END))
btn_clear.grid(row=row_val, column=col_val, sticky='nsew')


root.bind('<Return>', calculate)


for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


root.mainloop()