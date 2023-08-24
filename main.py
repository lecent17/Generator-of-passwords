# Import required libraries
from os import system
from passGen import PassGen


def main():
    system("cls")
    try:
        length: int = int(input(f'Введите длину пароля:\n'))
        is_special: bool = bool(int(input('Хотите ли вы использовать специальные символы?\n1. Да\n0. Нет\n')))
    except ValueError:
        print("Вы ввели неверные данные")
        exit(0)
    system("cls")
    passwords: list[str] = PassGen(is_special).generate(length)
    print(f'Сгенерированные пароли:')
    for index, pas in enumerate(passwords):
        print(f'{index}. {pas}')


if __name__ == '__main__':
    main()
