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
