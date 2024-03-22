s, n, res = input().split(), int(input()), []
def chunked(string, num):
    if len(string) < num:
        return [s]
    iter = len(string) // num + len(string) % num
    while iter > 0:
        row = []
        if len(string) == 1:
            num = 1
        for i in range(num):
            row.append(s[i])
        res.append(row)
        for j in range(num):
            del s[0]
        iter -= 1
    return(res)
print(chunked(s,n))