from Backend import Backend

directory = 'C:/Users/Will May/Documents'
backend = Backend()
backend.directory = directory
backend.file_type = 'pdf'
backend.search_string = 'cancer'
occurrences = backend.search_files(ignore_case = True)
for occurrence in occurrences:
    print(occurrence.text)