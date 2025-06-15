def copy_file_content(source, destination):
    with open(source, 'r') as src_file:
        content = src_file.read()
    with open(destination, 'w') as dest_file:
        dest_file.write(content)
