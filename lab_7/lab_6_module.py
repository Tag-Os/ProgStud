import os

def find_files_by_extension(directory, extension):
    """
    Находит файлы с заданным расширением в указанной директории и её поддиректориях.
    """
    if not extension.startswith('.'):
        extension = '.' + extension

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                yield os.path.join(root, file)
