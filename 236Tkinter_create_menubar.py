import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('menubar')

# command function
def save():
    print('save called')

def save_as():
    print('save as called')

def copy():
    print('copy called')

def cut():
    print('cut called')

def undo():
    print('undo called')

# menubar

#*************************simple menubar******************
#menubar = tk.Menu(win)
# menubar.add_command(label = 'Save', command = save)
# menubar.add_command(label = 'Save as', command = save_as)
# menubar.add_command(label = 'copy', command = copy)
# menubar.add_command(label = 'cut', command = cut)


# mainmenubar
main_menu = tk.Menu(win)
file_menu = tk.Menu(main_menu,tearoff = 0)


file_menu.add_command(label = 'Save', command = save)
file_menu.add_command(label = 'Save as', command = save_as)
file_menu.add_separator()
file_menu.add_command(label = 'copy', command = copy)
file_menu.add_command(label = 'cut', command = cut)

main_menu.add_cascade(label = 'file', menu = file_menu)


## edit menu
edit_menu = tk.Menu(main_menu)
edit_menu.add_command(label = 'undo', command = undo)
main_menu.add_cascade(label = 'edit', menu = edit_menu)

win.config(menu = main_menu)

win.mainloop()