def key_error():
    data = {'subject': 'computer', 'marks': 26}
    try:
        value = data['rollno.']  
    except KeyError as e:
        print("KeyError occurred:", e)
        value = 'Unknown'  
    return value


result = key_error()
print("Retrieved value:", result)
