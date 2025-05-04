d = {}

def len3():
    print("Length of dict: ", len(d))
    return len(d)

def add3(k, v):
    d[k] = v
    print(d)

def keys3():
    print("Keys: ",list(d.keys()))
    return list(d.keys())

def values3():
    print("Values: ",list(d.values()))
    return list(d.values())
