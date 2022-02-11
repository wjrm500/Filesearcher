import tkinter
from tkinter.filedialog import askdirectory
import sys
sys.path.append('.')

from backend.Backend import Backend

def ask_directory(evt):
    directory_entry_var.set(askdirectory())

def get_results(evt):
    backend = Backend()
    backend.directory = directory_entry_var.get()
    backend.file_types = [options[file_type_var.get()]]
    backend.search_string = search_string_entry.get()
    occurrences = backend.search_files(recursive = True, ignore_case = True)
    occurrences_text = '\n'.join([x.text for x in occurrences])
    results_var.set(occurrences_text)

root = tkinter.Tk()
frame = tkinter.Frame(master = root)

directory_button = tkinter.Button(master = frame, text = 'Select directory')
directory_button.bind('<Button-1>', ask_directory)
directory_entry_var = tkinter.StringVar()
directory_entry = tkinter.Entry(master = frame, textvariable = directory_entry_var, width = 50)
directory_entry.configure(state = 'disabled')

options = {
    'CSV files': 'csv',
    'Excel spreadsheets': 'xlsx',
    'PDF files': 'pdf',
    'PowerPoint presentations': 'pptx',
    'Text files': 'txt',
    'Word documents': 'docx'
}
file_type_var = tkinter.StringVar()
file_type_select = tkinter.OptionMenu(frame, file_type_var, *options.keys())

search_string_label = tkinter.Label(master = frame, text = 'Enter search string')
search_string_entry = tkinter.Entry(master = frame)

submit_button = tkinter.Button(master = frame, text = 'Submit')
submit_button.bind('<Button-1>', get_results)

results_var = tkinter.StringVar()
results_text = tkinter.Label(master = frame, textvariable = results_var)

frame.pack()
directory_button.pack()
directory_entry.pack()
file_type_select.pack()
search_string_label.pack()
search_string_entry.pack()
submit_button.pack()
results_text.pack()
root.mainloop()
