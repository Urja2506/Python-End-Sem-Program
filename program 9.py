def multiple_exceptions():

    try:
         number = int("string")
    except ValueError as e:
        print("ValueError:", e)

    try:
         result = "string" + 10
    except TypeError as e:
        print("TypeError:", e)

    try:
         l = [1, 2, 3]
         print(l[5])
    except IndexError as e:
        print("IndexError:",e)

    try:
         d = {"name": "Alice"}
         print(d["age"])
    except KeyError as e:
        print("KeyError:", e)

    try:
         result = 10 / 0
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)

multiple_exceptions()
