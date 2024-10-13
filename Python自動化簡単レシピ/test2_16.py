def search(findname):
    names = ["A太","B介","C子","D郎"]
    for i, name in enumerate(names):
        if name == findname:
            return i, name
    return -1, "見つかりませんでした。"

n, name = search("C子")
print(name,n,"番")

n, name = search("A子")
print(name,n,"番")
