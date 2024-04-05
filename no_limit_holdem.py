import random

# Определение рангов и мастей карт
suits = ['Черви', 'Бубны', 'Пики', 'Трефы']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']

# Создание колоды карт
deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

# Функция для перемешивания колоды
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# Функция для раздачи карт
def deal_cards(deck, number_of_cards):
    return [deck.pop() for _ in range(number_of_cards)]

# Функция для вывода карт игрока
def show_hand(hand):
    return ', '.join([f"{card['rank']} {card['suit']}" for card in hand])

# Функция для определения комбинаций в руке
def evaluate_hand(hand):
    # Здесь должна быть логика для определения комбинаций
    # ...
    pass

# Игровой процесс
def play_poker():
    # Перемешиваем колоду
    shuffled_deck = shuffle_deck(deck)

    # Раздаем карты игрокам
    player_hand = deal_cards(shuffled_deck, 2)
    opponent_hand = deal_cards(shuffled_deck, 2)

    # Выводим карты игроков
    print(f"Ваши карты: {show_hand(player_hand)}")
    print(f"Карты оппонента: {show_hand(opponent_hand)}")

    # Раздаем общие карты
    flop = deal_cards(shuffled_deck, 3)
    turn = deal_cards(shuffled_deck, 1)
    river = deal_cards(shuffled_deck, 1)

    # Выводим общие карты
    print(f"Flop: {show_hand(flop)}")
    print(f"Turn: {show_hand(turn)}")
    print(f"River: {show_hand(river)}")

    # Определяем победителя
    # ...

# Запуск игры
play_poker()
