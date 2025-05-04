st = set()

def slen2():
    print("Length of set:", len(st))
    return len(st)

def adds2(x):
    st.add(x)
    print(st)

def remove2(x):
    if x in st:
        st.remove(x)
        print(st)
    else:
        print("not found in the set.")
