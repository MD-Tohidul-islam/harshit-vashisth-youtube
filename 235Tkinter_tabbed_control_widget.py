# note book --- contain two pages
# page 1         page 2

# widgets        widgets

import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Tab control')
nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
nb.add(page1, text = 'one')
nb.add(page2, text = 'two')
nb.pack(expand = True, fill = 'both')

label1 = ttk.Label(page1, text = 'this is lable1:')
label1.grid(row = 0, column = 0)

entry1 = ttk.Entry(page1, width = 26)
entry1.grid(row =0 , column = 1)

label2 = ttk.Label(page2, text = 'this is lable2:')
label2.grid(row = 0, column = 0)

entry2 = ttk.Entry(page2, width = 26)
entry2 .grid(row =0 , column = 1)

win.mainloop()