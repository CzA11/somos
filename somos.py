import sys
v = sys.version

if "2.7" in v:
    from Tkinter import *
    import tkFileDialog
else:
    from tkinter import *
    import tkinter.filedialog
i_am_root = Tk("Somos")
text = Text(i_am_root)
text.grid()
def save_as_option():
    global text
    text_grab = text.get('1.0', 'end-1c')
    location_of_file_save = filedialog.asksaveasfilename()
    file_one = open(location_of_file_save, "w+")
    file_one.write(t)
    file_one.close()
save_button = Button(i_am_root, text = 'Save!', command = save_as_option)
save_button.grid()
i_am_root.mainloop()
