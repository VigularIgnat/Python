file_name="C:\\Users\\user\\Desktop\\text.txt"
with open(file_name) as file_object:
    for line in file_object:
        print(line.strip())
