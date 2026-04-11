import tkinter as tk
from tkinter import messagebox
from main import save_to_history, export_to_csv

root = tk.Tk()
root.title('Calculator')
root.geometry('300x500')

def disable_inputs():
    choice_value = choice.get()
    
    if choice_value == '5':
        entry1.config(state="disabled")
        entry2.config(state="disabled")
        expr_entry.config(state="normal")
    else:
        entry1.config(state="normal")
        entry2.config(state="normal")
        expr_entry.config(state="disabled")

label1 = tk.Label(root, text='Operation:', font=('arial', 10))
label1.pack(pady=5)

choice = tk.StringVar(value='1')

frame = tk.Frame(root)
frame.pack(pady=10)

add = tk.Radiobutton(frame, text='Add (+)', variable=choice, value='1', command=disable_inputs)
add.pack(anchor='w')

substract = tk.Radiobutton(frame, text='Subtract (-)', variable=choice, value='2', command=disable_inputs)
substract.pack(anchor='w')

multiply = tk.Radiobutton(frame, text='Multiply (*)', variable=choice, value='3', command=disable_inputs)
multiply.pack(anchor='w')

divide = tk.Radiobutton(frame, text='Divide (/)', variable=choice, value='4', command=disable_inputs)
divide.pack(anchor='w')

bodmas = tk.Radiobutton(frame, text='Expression (BODMAS)', variable=choice, value='5', command=disable_inputs)
bodmas.pack(anchor='w')

label2 = tk.Label(root, text='First Number:', font=('arial', 10))
label2.pack(pady=5)

entry1 = tk.Entry(root, width=30)
entry1.pack()

label3 = tk.Label(root, text='Second Number:', font=('arial', 10))
label3.pack(pady=5)

entry2 = tk.Entry(root, width=30)
entry2.pack()

label4 = tk.Label(root, text='Expression:', font=('arial', 10))
label4.pack(pady=5)

expr_entry = tk.Entry(root, width=30)
expr_entry.pack()

result_label = tk.Label(root, text='Result: ', font=('arial', 12, 'bold'))
result_label.pack(pady=10)

def calculate():
    try:
        choice_value = choice.get()
        
        if choice_value in ['1', '2', '3', '4']:
            x = int(entry1.get())
            y = int(entry2.get())
            
            if choice_value == '1':
                result = x + y
                expression = f"{x} + {y}"
            elif choice_value == '2':
                result = x - y
                expression = f"{x} - {y}"
            elif choice_value == '3':
                result = x * y
                expression = f"{x} * {y}"
            elif choice_value == '4':
                if y == 0:
                    messagebox.showerror('Error', 'Cannot divide by zero')
                else:
                    result = x / y
                    expression = f"{x} / {y}"
            
            save_to_history(expression, result)
            
        elif choice_value == '5':
            expression = expr_entry.get()
            result = eval(expression)
            save_to_history(expression, result)
        
        result_text = f"{int(result) if result == int(result) else result}"
        result_label.config(text=f'Result: {result_text}')
        messagebox.showinfo('Success', f'Result: {result_text}')
        
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers')
    except ZeroDivisionError:
        messagebox.showerror('Error', 'Cannot divide by zero')
    except Exception as e:
        messagebox.showerror('Error', f'Invalid input: {str(e)}')

def export():
    result = export_to_csv()
    if result:
        messagebox.showinfo('Success', 'History exported to history.csv')
    else:
        messagebox.showerror('Error', 'No history to export')

button = tk.Frame(root)
button.pack(pady=10)
tk.Button(button, text='Calculate', command=calculate, bg='green', fg='white', width=15).pack(side='left', padx=5)
tk.Button(button, text='Export to CSV', command=export, bg='blue', fg='white', width=15).pack(side='left', padx=5)

root.mainloop()