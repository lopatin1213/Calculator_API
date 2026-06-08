import addings
from sympy import *
import logging

import re
import sympy

def get_all_sympy_function_names():
    """Собирает имена всех встроенных функций и констант SymPy."""
    names = set()
    for name, obj in vars(sympy).items():
        if name.startswith('_'):
            continue
        if isinstance(obj, FunctionClass):
            names.add(name)
    # Сбор функций (как и раньше)
    def collect(module):
        for attr_name in dir(module):
            if attr_name.startswith('_'):
                continue
            try:
                attr = getattr(module, attr_name)
            except Exception:
                continue
            if callable(attr) or isinstance(attr, type):
                names.add(attr_name)
            elif hasattr(attr, '__module__') and 'sympy.functions' in getattr(attr, '__module__', ''):
                collect(attr)
    collect(sympy.functions)

    # Сбор констант (новое!)
    for name in dir(sympy):
        if name.startswith('_'):
            continue
        try:
            obj = getattr(sympy, name)
        except Exception:
            continue
        # Проверяем, что это константа, а не функция или класс
        if hasattr(obj, 'is_constant') and obj.is_constant:
            if not callable(obj) and not isinstance(obj, type):
                names.add(name)

    # Твои любимые ручные дополнения
    names.update(['sqrt', 'log', 'ln', 'Abs', 'sign', 'floor', 'ceiling'])
    return names

def insert_multiplication_signs(expr: str, extra_functions=None) -> str:
    """
    Вставляет знаки умножения с учётом неявного умножения.
    Поддерживает латиницу и кириллицу в именах переменных.
    Защищает все известные SymPy-функции и константы от разбиения.
    """
    func_set = get_all_sympy_function_names()  # теперь там и функции, и константы
    if extra_functions:
        func_set.update(extra_functions)

    sorted_funcs = sorted(func_set, key=len, reverse=True)
    func_pattern = '|'.join(re.escape(f) for f in sorted_funcs)

    LETTER = r'[A-Za-zА-Яа-яёЁ_]'
    LETTER_DIGIT = r'[\dA-Za-zА-Яа-яёЁ_]'

    # === ШАГ 1: Защита известных имён (функций и констант) ===
    protected = {}
    def protect_known(match):
        name = match.group(0)
        if name not in func_set:
            return name
        placeholder = f'\ue000{len(protected)}\ue001'
        protected[placeholder] = name
        return placeholder

    expr = re.sub(r'[A-Za-z_]\w*', protect_known, expr)

    # === ШАГ 2: Правила вставки умножения ===
    # Явно вставляем * между цифрой/буквой и известным именем перед '('
    expr = re.sub(rf'(\d)({func_pattern})(?=\()', r'\1*\2', expr)
    expr = re.sub(rf'({LETTER})({func_pattern})(?=\()', r'\1*\2', expr)

    # Основные правила с кириллицей
    expr = re.sub(rf'(\d)({LETTER})', r'\1*\2', expr)                # 2x, 2я
    # РАЗРЫВАЕМ ВСЕ ЦЕПОЧКИ БУКВ (кроме защищённых имён)
    expr = re.sub(rf'({LETTER})(?={LETTER})', r'\1*', expr)         # a*b*c, а*я
    expr = re.sub(rf'({LETTER_DIGIT})(\()', r'\1*\2', expr)         # a(, 3(, я(
    expr = re.sub(rf'(\))({LETTER_DIGIT}\()', r'\1*\2', expr)       # )a, )(, )я

    # === ШАГ 3: Возвращаем защищённые имена на место ===
    for placeholder, name in protected.items():
        expr = expr.replace(placeholder, name)

    return expr

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
            equation = insert_multiplication_signs(equation)
            print(equation)
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


