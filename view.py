import calculate

MENU_ITEMS = {
    "Q": "Выход",
    "+": "Сложение",
    "-": "Вычитание",
    "*": "Умножение",
    "/": "Деление",
    "S": "Функция MS",
    "R": "Функция MR"
}


def print_memory():
    print(f"Число в памяти: {calculate.memory}")


def menu():
    for index, item in MENU_ITEMS.items():
        print(f"{index} - {item}")
    print("Выберите пункт меню: ", end="")


def print_char(ch):
    print(f"Введите {ch}: ", end="")
