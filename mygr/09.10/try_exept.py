file_name="C:\\Users\\user\\Desktop\\text2.txt"

try:
    with open(file_name) as file_object:
        contents=file_object.read()
       
    print(contents)
except FileNotFoundError:
    print(f"Sorry, this fille {file_name} is broke")
