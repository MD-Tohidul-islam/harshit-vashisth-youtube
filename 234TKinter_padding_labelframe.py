import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('label frame')
label_list = ['what is your name?', 'what is your age? ', 'what is your gender',
              'country','state','city']
label_frame = ttk.LabelFrame(win, text = 'Enter your details: ')
label_frame.grid(row = 0, column = 0)
for i in range(len(label_list)):
    cur_label = 'label'+str(i) # label variable
    cur_label = ttk.Label(label_frame, text=label_list[i])
    cur_label.grid(row=i, column=0, sticky=tk.W, padx = 10, pady = 5)

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
    cur_entry_box = ttk.Entry(label_frame, width = 16, textvariable = user_info[i])
    cur_entry_box.grid(row =counter, column = 1 , padx = 10, pady = 5)
    counter +=1
def submit():
    for i in user_info:
        print(user_info.get(i).get())
submit_button = ttk.Button(win, text = 'submit', command = submit)
submit_button.grid(row= 6, column = 2)


win.mainloop()
