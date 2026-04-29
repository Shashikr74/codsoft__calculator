# file: calculator_gui.py
import tkinter as tk
from calculator_backend import calculate

def on_click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def compute():
    try:
        expression = entry.get()
        # parse simple format: number operator number
        for op in ['+', '-', '*', '/']:
            if op in expression:
                a, b = expression.split(op)
                result = calculate(float(a), float(b), op)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
                return
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Invalid")

# GUI setup
root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=25, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','C','=','+'
]

row, col = 1, 0
for b in buttons:
    if b == 'C':
        action = clear
    elif b == '=':
        action = compute
    else:
        action = lambda x=b: on_click(x)

    tk.Button(root, text=b, width=5, height=2, command=action)\
        .grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
