from Backend import Backend

directory = 'C:/Users/Will May/Documents'
backend = Backend()
backend.directory = directory
backend.file_type = 'txt'
backend.search_string = 'Hello'
results = backend.search_files()
print(results)