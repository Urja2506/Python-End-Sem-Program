def file_error():
    filename = "file.txt"
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError as e:
        print("FileNotFoundError occurred:", e)

file_error()

