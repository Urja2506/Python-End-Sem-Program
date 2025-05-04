lt = []

def append1(x):
    lt.append(x)
    print(lt)

def extend1(l):
    lt.extend(l)
    print(lt)

def pop():
    if lt:
        r = lt.pop()
        print(lt)
    else:
        print("List is empty. Cannot pop.")

def remove1(x):
    if x in lt:
        lt.remove(x)
        print(lt)
    else:
        print("not found in lt")
