import os
#Сам код
def find_files(directory, extension):
    
    if not extension.startswith('.'):
        extension = '.' + extension

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                yield os.path.join(root, file)

#Юзание
directory = os.path.join('.', 'lab_6')
extension = '.txt'

print(f"Файлы с расширением {extension} в каталоге {directory}:")
for file_path in find_files(directory, extension):
    print(file_path)
