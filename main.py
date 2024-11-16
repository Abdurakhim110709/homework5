from decouple import Config
from logic import GuessNumberGame

def main():
    # Загружаем параметры из конфигурации
    config = Config


    min_number = config.get ('min_number', cast=int)
    max_number = config.get ('max_number', cast=int)
    attempts = config.get('attempts', cast=int)
    initial_capital = config.get('initial_capital', cast=int)

    # Создаем объект игры
    game = GuessNumberGame(min_number, max_number, attempts, initial_capital)

    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Диапазон чисел от {min_number} до {max_number}. У вас {attempts} попыток.")
    print(f"Ваш начальный капитал: {initial_capital}.")

    while attempts > 0 and game.capital > 0:
        print(f"\nВаш капитал: {game.capital}")
        print(f"Осталось попыток: {attempts}")

        # Запрос ставки и числа
        try:
            bet = int(input(f"Сделайте ставку (текущий капитал: {game.capital}): "))
            guess = int(input(f"Угадайте число от {min_number} до {max_number}: "))
        except ValueError:
            print("Пожалуйста, введите правильное число.")
            continue

        # Обрабатываем попытку
        result = game.play_round(guess, bet)
        print(result)
        attempts -= 1

        if game.capital <= 0:
            print("Вы проиграли все деньги. Игра окончена!")
            break

        if attempts == 0:
            print("У вас закончились попытки.")
            break

    print("Спасибо за игру!")


if __name__ == "__main__":
    main()
