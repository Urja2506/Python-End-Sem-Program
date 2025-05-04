def attribute_error():
    text = "hello"
    try:
        result = text.delete() 
    except AttributeError as e:
        print("AttributeError occurred:", e)

attribute_error()

