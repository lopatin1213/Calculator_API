from string import printable, ascii_uppercase

import logging
def to_10(n, ss):
    print(n, ss)
    ss = int(ss)
 #   logging.error(f"{type(n)}, {type(ss)}")#
    try:
        return int(str(n), ss)
    except Exception:
#        logging.error(type(e), str(e))
        raise ValueError(f"Для {ss} системы счисления можно использовать только символы {printable[:ss]}")





def to_2_36(n,ss):
    # Функция принимает число n,
    # переводит в систему счисления равной ss
    # И возвращает число в виде строки
    ss = int(ss)
    alph = "0123456789" + ascii_uppercase
    res = ''
    while n > 0:
        res = alph[n % ss] + res
        n //= ss
    return res


def calculate_sch(first, second, type, ss):
    try:
        a = to_10(first, ss)
        logging.info(a)
        b = to_10(second, ss)
        logging.info(b)
        if type == "+":
            result = a + b
        elif type == "-":
            result = a - b
        elif type == "*":
            result = a * b
        elif type == "/":
            result = a // b
            result = int(result)
        else:
            raise ValueError("Такого нет")
        #        logging.info(result)
        result = to_2_36(result, ss)
        logging.info(result)
        return f"{result}"

    #       logging.info(window.label_sch_result.text())
    # update_history()

    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return str(e)


def perevod_to(num, ss1, ss2):
    try:
        a = to_10(num, ss1)

        result = to_2_36(a, ss2)
        #       logging.info(result)
        return f"{result}"

    #      logging.info(window.label_sch_result.text())
    # update_history()

    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return str(e)