from datetime import datetime, timedelta
d = datetime.strptime(input(), '%d.%m.%Y')
print((d - timedelta(days=1)).strftime('%d.%m.%Y'))
print((d + timedelta(days=1)).strftime('%d.%m.%Y'))