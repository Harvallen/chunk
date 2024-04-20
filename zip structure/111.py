def size_coverter(size):
    count = 0
    d = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB'}
    while size / 1024 > 1:    
        size /= 1024
        count += 1
    return int(size), d[count]
    
print(*size_coverter(5600000000))