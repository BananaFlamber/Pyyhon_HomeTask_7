import calculate
from input import menu_input, check_menu_item, input_value, input_op
from view import menu, print_char, print_memory


while True:
    print_memory()
    menu()
    menu_item = menu_input()
    if not check_menu_item(menu_item):
        # обработка неправильного выбора меню
        print('Такого пункта нет')
        continue
    elif menu_item == 'Q':
        break

    print_char("a")
    a = input_value()
    print_char("b")
    b = input_value()

    calculate.memory = calculate.calculate(a, b, menu_item)
    print(f"Результат операции: {a} {menu_item} {b} = {calculate.memory}")
