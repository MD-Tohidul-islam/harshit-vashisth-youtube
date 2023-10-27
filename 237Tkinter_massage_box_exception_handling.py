import tkinter as tk
from  tkinter import ttk
from tkinter import messagebox as mbx

win = tk.Tk()

# label frame
label_frmae = ttk.LabelFrame(win, text = 'contact detail')
label_frmae.grid(row = 0, column = 0, padx = 40, pady = 10)

# labels
name_label = ttk.Label(label_frmae, text = 'Enter your name: ', font = ('Helvetica', 14))
age_label = ttk.Label(label_frmae, text = 'Enter your age: ', font = ('14'))


# entry box variable
name_var = tk.StringVar()
age_var = tk.StringVar()

# entry boxes
name_entry = ttk.Entry(label_frmae, width = 30, textvariable = name_var)
age_entry = ttk.Entry(label_frmae, width = 20, textvariable = age_var)

# grid
name_label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = tk.W)
age_label.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = tk.W)
name_entry.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = tk.W)
age_entry.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = tk.W)

def submit():
    name = name_var.get()
    age = age_var.get()
    if name == '' or age == '':
        mbx.showerror('Error', 'please fill name and age')
    else:
        try:
            age = int(age)
        except ValueError:
            mbx.showerror('Error','only digits are allowed age fill')
        else:
            if age < 18:
                mbx.showwarning('Warning', 'you age not able to visit')
    mbx.showinfo('Info',f'your name is {name} and your age is  {age}')


submin_btn = ttk.Button(win, text = 'submit', command = submit)
submin_btn.grid(row = 1, columnspan = 2 , padx = 40)



win.mainloop()
