import addings
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import logging

def plot_linear_equation(a, b, c):
    """
    Строит график линейного уравнения ax + by + c = 0.
    """
    try:
        # Генерируем диапазон значений x с высокой точностью
        x = np.linspace(-10000, 10000, 100000)  # 100000 точек между -10000 и 10000
        # Вычисляем соответствующие значения y
        y = (-c - a * x) / b
        # Строим график
        fig, ax = plt.subplots()
        ax.plot(x, y, label=f"{a}x + {b}y + {c} = 0")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(True)
        ax.legend()
    
        # Устанавливаем начальные границы оси X и Y
        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])
        b_str = str(b)
        # Центрируем график относительно точки (0, b)
        center_x = 0
        if not "-" in b_str:
            center_y = -c / b
        else:
            center_y = -c / b
        center_y = float(center_y)  # Убеждаемся, что center_y является числом
        center_x = float(center_x)
        ax.set_xlim(center_x - 10, center_x + 10)  # Центрирование по оси X
        ax.set_ylim(center_y - 10, center_y + 10)  # Центрирование по оси Y
    
        # Выделяем оси x и y
        ax.axhline(0, color='black', linewidth=1)  # Горизонтальная ось y=0
        ax.axvline(0, color='black', linewidth=1)  # Вертикальная ось x=0
    
        # Помещаем точку (0, b) в центр графика
        ax.scatter(center_x, center_y, s=50, color='blue', marker='o', label=f'(0, {center_y})')  # Размер точки s=50
        ax.legend()
        y_1 = 0
        if not "-" in b_str:
            x_1 = -c / a
        else:
            x_1 = -c / a
        x_1 = float(x_1)
        ax.scatter(x_1, y_1, s=50, color='red', marker='o', label=f'({x_1}, 0)')
        ax.legend()
    
        # Назначаем события мыши для динамического масштабирования
        def on_motion(event):
            if event.inaxes:
                # Получаем текущие границы оси X
                xmin, xmax = ax.get_xlim()
                # Проверяем, достигнута ли граница оси X
                if event.xdata > xmax - 0.01 * (xmax - xmin) or event.xdata < xmin + 0.01 * (xmax - xmin):
                    # Расширяем границы оси X
                    ax.set_xlim(xmin - 0.05 * (xmax - xmin), xmax + 0.05 * (xmax - xmin))
                    fig.canvas.draw_idle()
    
        # Привязываем событие движения мыши
        fig.canvas.mpl_connect('motion_notify_event', on_motion)
    
        plt.show()
    except Exception as e:
        raise Exception(e)


import re


def transform_equation(lhs, rhs):
    """
    Преобразует уравнение вида y = kx + b в b = y - kx.

    Аргументы:
    - lhs: левая сторона уравнения.
    - rhs: правая сторона уравнения.

    Возвращает:
    Преобразованное уравнение.
    """
    # Регулярное выражение для извлечения коэффициентов и переменных
    pattern = r'(?P<y>\w+)\s*=\s*((?P<k>[+-]?\d*\.*\d*)?\s*\*\s*)?(?P<x>\w+)(?:\s*[+-]?\s*(?P<b>-?\d*\.*\d*))?'
    # Объединяем левую и правую стороны в одно уравнение
    equation = f"{lhs} = {rhs}"
    
    match = re.match(pattern, equation)
    
    if not match:
        return "Неверный формат уравнения."
    
    y = match.group('y')
    k = match.group('k') or '1'  # Если коэффициент не указан, считаем его равным 1
    x = match.group('x')
    b = match.group('b') or '0'
    
    transformed_eq = f"-{k}*{x}+{y}={b}"
    return transformed_eq


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
            return formatted_result
        else:
            # Если решение не найдено
            return "No solves"
        
    
    # Обновляем историю
    
    except Exception as e:
        return str(e)

