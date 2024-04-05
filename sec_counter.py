from datetime import datetime, timedelta
t = input()
time = timedelta(seconds=int(t[-2:]), minutes=int(t[-5:-3]), hours=int(t[:2]))
print(time.seconds)