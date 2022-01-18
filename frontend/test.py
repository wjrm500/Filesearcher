import tkinter
from tkinter.filedialog import askdirectory

window = tkinter.Tk()
frame = tkinter.Frame(master = window)
directory = askdirectory()
print(directory)