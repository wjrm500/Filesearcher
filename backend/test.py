from Backend import Backend

directory = 'C:/Users/wjrm5/Documents'
backend = Backend()
backend.directory = directory
backend.file_types = ['docx', 'txt']
backend.search_string = 'Catan'
occurrences = backend.search_files(recursive = True, ignore_case = True)
for occurrence in occurrences:
    print(occurrence.text)