def module_error():
    try:
        import addition
    except ModuleNotFoundError as e:
        print("ModuleNotFoundError occurred:", e)

module_error()

