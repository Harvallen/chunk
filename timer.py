from datetime import datetime, time, timedelta
n = datetime.strptime(input(), '%H:%M:%S')
print((n + timedelta(seconds=int(input()))).strftime('%H:%M:%S'))