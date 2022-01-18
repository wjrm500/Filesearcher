from Backend import Backend

directory = 'C:/Users/Will May/Documents'
backend = Backend()
backend.directory = directory
backend.file_type = 'docx'
backend.search_string = 'dog'
occurrences = backend.search_files()
for occurrence in occurrences:
    print(occurrence.text)