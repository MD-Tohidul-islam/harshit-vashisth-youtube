import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win = tk.Tk()
win.title('GUI')

# create labels
name_label = ttk.Label(win, text = 'Enter your name: ')
name_label.grid(row=0, column=0,sticky=tk.W)

age_label = ttk.Label(win, text = 'Enter your age: ')
age_label.grid(row=1, column=0, sticky=tk.W)

email_label = ttk.Label(win, text='Enter your email: ')
email_label.grid(row=2,column=0,sticky=tk.W)

gender_lebel = ttk.Label(win, text='Select your gender: ')
gender_lebel.grid(row=3,column=0,sticky=tk.W)

# create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=16,textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

age_var = tk.IntVar()
age_entrybox = ttk.Entry(win, width=16,textvariable=age_var)
age_entrybox.grid(row=1, column=1)

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=16,textvariable=email_var)
email_entrybox.grid(row=2, column=1)

# create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=14,textvariable = gender_var,state='readonly')
gender_combobox['values'] = ('male','female','other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

# radio button
user_type = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text='Student', value='Student',variable = user_type)
radiobtn1.grid(row=4,column=0)
radiobtn1 = ttk.Radiobutton(win, text='Teacher', value='Teacher',variable = user_type)
radiobtn1.grid(row=4,column=1)

# check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text='check if you want to subscribe to you newsletter',variable = checkbtn_var)

checkbtn.grid(row=5, columnspan =3)

# create button
# def action():
#     user_name = name_var.get()
#     user_age = age_var.get()
#     user_email = email_var.get()
#     print(f'{user_name}, {user_age} years old ,{user_email}')
#     user_gender = gender_var.get()
#     usertype = user_type.get()
#     if checkbtn_var.get() == 0:
#         subscribe = 'No'
#     else:
#         subscribe = 'Yes'
#     print(user_gender,user_gender,subscribe)
#
#     with open('user.txt','a') as f:
#         f.write(f'{user_name}, {user_age} year old, {user_email}, {user_gender},'
#                 f'{usertype}, {subscribe}\n')
#     name_entrybox.delete(0, tk.END)
#     age_entrybox.delete(0, tk.END)
#     email_entrybox.delete(0, tk.END)
#
#     # color
#     name_label.configure(foregroun = 'Blue', backgroun = 'Black')
#     #submit_button.configure(foreground='Green')

# write to csv files
def action():
    user_name = name_var.get()
    user_age = age_var.get()
    user_email = email_var.get()
    user_gender = gender_var.get()
    usertype = user_type.get()
    if checkbtn_var.get() == 0:
        subscribe = 'No'
    else:
        subscribe = 'Yes'

    # write to csv file
    with open('user.csv','a',newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['UserName','User Email','User age','User gender',
                                                'User type', 'Subscribe'])
        if os.stat('user.csv').st_size == 0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'UserName': user_name,
            'User Email': user_email,
            'User age': user_age,
            'User gender': user_gender,
            'User type': usertype,
            'Subscribe': subscribe
        })

    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)

    # color
    name_label.configure(foregroun = 'Blue', backgroun = 'Black')
    print(user_gender,user_gender,subscribe)
submit_button = ttk.Button(win, text='Submit',command = action)
submit_button.grid(row=6,column=0)




win.mainloop()