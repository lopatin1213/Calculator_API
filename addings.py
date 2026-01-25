import logging
import sys
from decimal import Decimal, getcontext


from sympy import Float, Integer

# from UI import NewApp
history = []


def get_root_degree(window):
    degree, ok_pressed = QInputDialog.getInt(window, "Корень", "Какая степень корня?")
    if ok_pressed:
        window.entry.setText(f"{degree}√")
    else:
        print("Отмена")

# def
def dynamic_precision(value):
    getcontext().prec = 30
    
    if isinstance(value, (int, float)):
        
        decimal_value = Decimal(str(value))
        order = int(decimal_value.adjusted())
        rounded_value = decimal_value.normalize()
        
        precision = max(6, -order + 6)
        logging.info(format(rounded_value, f'.{precision}f').rstrip('0').rstrip('.'))
        return format(rounded_value, f'.{precision}f').rstrip('0').rstrip('.')
    
    elif isinstance(value, complex):
        real_part = dynamic_precision(value.real)
        imag_part = dynamic_precision(value.imag)
        return complex(real_part, imag_part)
    
    elif isinstance(value, str):
        logging.info(f'Это строка {value}')
        return value
    
    elif isinstance(value, list) or isinstance(value, tuple):
        return type(value)(map(dynamic_precision, value))
    elif isinstance(value, Float):
        value = float(value)
        decimal_value = Decimal(str(value))
        order = int(decimal_value.adjusted())
        rounded_value = decimal_value.normalize()
        precision = max(6, -order + 6)
        logging.info(format(rounded_value, f'.{precision}f').rstrip('0').rstrip('.'))
        return format(rounded_value, f'.{precision}f').rstrip('0').rstrip('.')
    elif isinstance(value, Integer):
        value = float(value)
        decimal_value = Decimal(str(value))
        order = int(decimal_value.adjusted())
        rounded_value = decimal_value.normalize()
        precision = max(6, -order + 6)
        logging.info(format(rounded_value, f'.{precision}f').rstrip('0').rstrip('.'))
        return format(rounded_value, f'.{precision}f').rstrip('0').rstrip('.')
    else:
        type_of = type(value)
        logging.info(f'Не определён тип {type_of}')
        return value






def format_number(num):
    try:
        # Проверяем условие вывода числа в экспоненциальной форме
        num = float(num)
        if (abs(num) >= 1000000000 or abs(num) <= 0.00001) and num != 0:
            # Переводим число в научную нотацию
            scientific_str = "{:.9E}".format(num)
            mantissa, exponent = scientific_str.split("E")
            return "{}*10^{}".format(float(mantissa), int(exponent))
        else:
            # Просто возвращаем само число
            return str(num)
    except Exception as e:
        return num


def clear_errors(window):
    """Очищает поле ошибок."""
    history_ui = HistoryandError()
    history_ui.error_text.clear()

