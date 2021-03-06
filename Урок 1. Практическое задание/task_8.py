"""
Задание 8.	Определить, является ли год, который ввел пользователем,
високосным или не високосным.

Подсказка:
Год является високосным в двух случаях: либо он кратен 4,
но при этом не кратен 100, либо кратен 400.

Попробуйте решить задачу двумя способами:
1. Обычное ветвление


П.С. - Тернарные операторы, также известные как условные выражения,
представляют собой операторы, которые оценивают что-либо на основе условия,
являющегося истинным или ложным. Он был добавлен в Python в версии 2.5 .
Он просто позволяет протестировать условие в одной строке,
заменяя многострочное if-else, делая код компактным.
"""


# 1. Обычное ветвление
try:
    user_year = int(input("Please type the year - "))
    if (user_year % 4 == 0 and not user_year % 100 == 0) or user_year % 400 == 0:
        is_leap = True
    else:
        is_leap = False

    if is_leap is True:
        print("Year is leap")
    else:
        print("Year isn't leap.")
except ValueError:
    print("You entered an incorrect value.")


# 2. Тернарный оператор
try:
    user_year = int(input("Please type the year - "))
    is_leap = True if \
        (user_year % 4 == 0 and not user_year % 100 == 0) or user_year % 400 == 0 \
        else False

    if is_leap is True:
        print("Year is leap")
    else:
        print("Year isn't leap.")
except ValueError:
    print("You entered an incorrect value.")
