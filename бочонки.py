import random
import logging
import keyboard

# Настройка логгирования
logging.basicConfig(filename='barrel_game.log', level=logging.INFO)


# Функция для получения ввода от пользователя
def get_input():
    while True:
        try:
            n = int(input("Введите количество бочек (целое положительное число): "))
            if n > 0:
                return n
            else:
                print("Введите положительное число!")
        except ValueError:
            print("Введите целое число!")


# Функция-генератор для рисования бочек
def draw_barrel(n):
    barrel_sequence = list(range(1, n+1))
    random.shuffle(barrel_sequence)
    for barrel in barrel_sequence:
        yield barrel  # Возвращаем текущий номер бочки
        keyboard.wait('Enter')  # Ждем нажатия клавиши Enter


# Основная функция программы
def main():
    n = get_input()
    barrel_drawer = draw_barrel(n)
    for _ in range(n):
        barrel = next(barrel_drawer)
        print(f"Вытащен бочонок с номером {barrel}")
        logging.info(f"Бочонок с номером {barrel} был вытащен")

if __name__ == "__main__":
    main()