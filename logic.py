import random

class GuessNumberGame:
    def __init__(self, min_number, max_number, attempts, initial_capital):
        self.min_number = min_number
        self.max_number = max_number
        self.attempts = attempts
        self.capital = initial_capital
        self.secret_number = random.randint(self.min_number, self.max_number)

    def play_round(self, guess, bet):
        """Обрабатывает одну попытку игрока."""
        if bet > self.capital:
            return "Недостаточно средств для ставки!"

        if guess == self.secret_number:
            self.capital += bet
            return f"Вы угадали! Ваш новый капитал: {self.capital}"
        else:
            self.capital -= bet
            return f"Не угадали. Ваш новый капитал: {self.capital}"

    def reset_game(self):
        """Сбрасывает игру и генерирует новое случайное число."""
        self.secret_number = random.randint(self.min_number, self.max_number)
        self.capital = initial_capital

