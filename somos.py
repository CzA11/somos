import sys
"""
Traceback (most recent call last):
  File "/Users/chantzanderson/Documents/somos.py", line 2, in <module>
    v = sys.python_version
AttributeError: module 'sys' has no attribute 'python_version'
|
|
|--- Fixed. It appears ' python_version' is now simply 'version'
"""
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


"""
Running errors:

1. sys missing 'python version'  - Fixed
2. tkinter.tkFileDialog does not exist - Fixed
3. error while saving - Open
---------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/chantzanderson/Documents/somos.py", line 2, in <module>
    v = sys.python_version
AttributeError: module 'sys' has no attribute 'python_version'
|
|
|--- Fixed. It appears ' python_version' is now simply 'version'


Traceback (most recent call last):
  File "/Users/chantzanderson/Documents/somos.py", line 18, in <module>
    import tkinter.tkFileDialog
ModuleNotFoundError: No module named 'tkinter.tkFileDialog'
|
|
|--- Fixed - Syntax error. should be: tkinter.filedialog


Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 1705, in __call__
    return self.func(*args)
  File "/Users/chantzanderson/Documents/somos.py", line 25, in save_as_option
    location_of_file_save = tkFileDialog.asksaveasfilename()
NameError: name 'tkFileDialog' is not defined
|
|
|--- Open
"""
