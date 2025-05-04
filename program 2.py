def name_error():
    a = 10
    b = 5
    try:
        result = a + b + c
    except NameError as e:
        print("NameError occurred:", e)
        result = a + b 
    return result

value = name_error()
print("Final result:", value)
