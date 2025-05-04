def value_error():
    s = "abc"  
    try:
        num = int(s)  
    except ValueError as e:
        print("ValueError occurred:", e)

value_error()

