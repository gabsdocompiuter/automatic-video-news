def filename(filename: str, extension: str) -> str:
    if extension[0:1] != '.':
        extension = '.' + extension

    filename = filename.replace(extension, '')
    
    return filename + extension