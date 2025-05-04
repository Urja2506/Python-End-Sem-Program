def index_error():
    items = [10, 20, 30]
    try:
        value = items[5]  
    except IndexError as e:
        print("IndexError occurred:", e)

index_error()

