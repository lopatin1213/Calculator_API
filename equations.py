import addings
from sympy import *
import logging



import re


def solve_system_of_equations(equations_str):
    try:
        # Получаем уравнения из поля ввода

        logging.info(f"Полученная строка уравнений: {equations_str}")
        if equations_str == "":
            return
        # Проверяем наличие запятых в строке

        # Разбиение строки на отдельные уравнения
        equations_list = equations_str.split(' ')
        logging.info(f"Разбито на уравнения: {equations_list}")

        # Преобразование уравнений в объекты Sympy
        expressions = []
        used_variables = set()  # Множество переменных, используемых в уравнениях
        for equation in equations_list:
            logging.info(f"Преобразование уравнения: {equation}")
            equation = equation.replace('=', '==')
            equation = re.sub(r'(\d+)([A-Za-zА-ЯЁа-яё])', r'\1*\2', equation)
            lhs, rhs = equation.split('==')
            logging.info(str(lhs))
            logging.info(str(rhs))
            expressions.append(Eq(sympify(lhs), sympify(rhs)))
            logging.info(f"Добавлено уравнение: {expressions[-1]}")

            # Определяем переменные, участвующие в текущем уравнении
            used_variables.update(list(expressions[-1].free_symbols))

        logging.info(f"Переменные, задействованные в уравнениях: {used_variables}")

        # Проверка на недоопределённость системы


        # Решаем систему уравнений
        solution = solve(expressions, used_variables)
        logging.info(f"Решение системы уравнений: {solution}")

        if solution:
            # Применяем dynamic_precision к каждому значению
            logging.info(str(solution))
            if isinstance(solution, list):
                num = []  # Список для хранения результирующих словарей

                for x in solution:
                    # Применяем точность к каждому решению
                    numeric_dict = {var: addings.dynamic_precision(sol.evalf()) for var, sol in x.items()}

                    # Добавляем полученный словарь в список
                    num.append(numeric_dict)

                # Теперь мы имеем список словарей в переменной num
                # Нам нужно объединить их в единую строку формата "var=value"
                results = []
                for dct in num:
                    # Для каждого словаря создадим строки вида "var=value"
                    for var, val in dct.items():
                        results.append(f"{var}={val}")

                # Объединяем все полученные строки в одну общую строку
                formatted_result = ", ".join(results)

                logging.info(str(formatted_result))
            else:
                numeric_dict = {var: addings.dynamic_precision(sol.evalf()) for var, sol in solution.items()}
                logging.info(f"Применение динамической точности: {numeric_dict}")

                # Форматируем результат для отображения
                formatted_result = ', '.join(f'{var}={val}' for var, val in numeric_dict.items())
            logging.info(f"Форматированный результат: {formatted_result}")

            # Выводим решение
            return f"{formatted_result}"
        else:
            # Если решение не найдено
            return "Решение не найдено."




    # Обновляем историю

    except Exception as e:
        logging.error(str(e))
        return str(e)


