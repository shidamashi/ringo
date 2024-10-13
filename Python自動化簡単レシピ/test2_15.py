def calc(max):
    a = 1
    while a < max:
        a = a*2
    return a

ans = calc(1000)
print("1000を超えた直後の値は",ans)
