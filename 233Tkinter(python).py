import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('loop')
label_list = ['what is your name?', 'what is your age? ', 'what is your gender',
              'country','state','city']

for i in range(len(label_list)):
    cur_label = 'label'+str(i) # label variable
    cur_label = ttk.Label(win, text=label_list[i])
    cur_label.grid(row=i, column=0, sticky=tk.W)

# create a entry box
user_info = {
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'gender':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar()
}
counter = 0
for i in user_info:
    cur_entry_box = 'entry'+i # for entry variable
    cur_entry_box = ttk.Entry(win, width = 16, textvariable = user_info[i])
    cur_entry_box.grid(row =counter, column = 1 )
    counter +=1
def submit():
    for i in user_info:
        print(user_info.get(i).get())
submit_button = ttk.Button(win, text = 'submit', command = submit)
submit_button.grid(row= 6, column = 2)


win.mainloop()
