from Backend import Backend

directory = 'C:/Users/Will May/Documents'
backend = Backend()
backend.directory = directory
backend.file_types = ['docx', 'txt']
backend.search_string = ''
occurrences = backend.search_files(recursive = True, ignore_case = True)
for occurrence in occurrences:
    print(occurrence.text)