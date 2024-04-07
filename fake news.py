from datetime import datetime, timedelta

def choose_plural(amount, variants):
    variant = 2
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    return '{} {}'.format(amount, variants[variant])

release_date = datetime(2022,11,8,12)
now_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
difference = release_date - now_date

message = 'До выхода курса осталось: '
dec_days = ('день', 'дня', 'дней')
dec_hours = ('час', 'часа', 'часов')
dec_minutes = ('минута', 'минуты', 'минут')

if difference != abs(difference) or not difference:
    print('Курс уже вышел!')
elif difference.days >= 1:
    if difference.seconds >= 3600:                    # 3600 секунд в одном часе
        print(f'{message}{choose_plural(difference.days, dec_days)} и {choose_plural(difference.seconds // 3600, dec_hours)}')
    else:
        print(f'{message}{choose_plural(difference.days, dec_days)}')
elif difference.seconds >= 3600:
    if difference.seconds % 3600 == 0:
        print(f'{message}{choose_plural(difference.seconds // 3600, dec_hours)}')
    else:
        print(f'{message}{choose_plural(difference.seconds // 3600, dec_hours)} и {choose_plural((difference.seconds - (difference.seconds // 3600) * 3600) // 60, dec_minutes)}')
elif difference.seconds < 3600:
    print(f'{message}{choose_plural((difference.seconds - (difference.seconds // 3600) * 3600) // 60, dec_minutes)}')