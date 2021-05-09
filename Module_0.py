import numpy as np

number = np.random.randint(1, 101)

"""
# Сначала делим весь диапазон на 2 с помощью целочисленного деления.
# Потом в зависимости от того если число больше или меньше temp сдвигаем к нему нижнию или верхнюю границу к диапазона.
# Далее сумируем нижний и верхний диапазоны и снова делим целочисленно на 2.
# Цикл повторяеться до нахождения цисла.
"""


def game_core(number):

    count = 1
    minimum = 1
    maximum = 101
    temp = 50

    while temp != number:
        count += 1
        if temp > number:
            maximum = temp
        elif temp < number:
            minimum = temp
        temp = (minimum + maximum) // 2
    return count


print(f"Компьютер отгадал число за {game_core(number)} попыток")

print('-------------------------------------')


def score_game(game_core):

    # Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число

    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Наш счетовод угадывает число в среднем за {score} попыток")
    return score


score_game(game_core)
