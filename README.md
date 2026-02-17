
https://calculator-api-mm7b.onrender.com/
ВСЕ ДАННЫЕ ПЕРЕДОВАТЬ В JSON

class CalcRequests(BaseModel):
    expr: str
@app.post("/calculate/")
Решает обычные примеры + функции из библиотеки sympy(['pi','sqrt', 'exp', 'ln', 'log', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan',
            'rad', 'deg', 'sinh', 'cosh', 'tanh',
                      'Si', 'Ci', 'Ei', ].
Пример запроса: POST /solve_equations/
    {
        "expr": "2+2"
    }
class EquationsRequests(BaseModel):
    equations: str
@app.post("/solve_equations/")

Решает систему уравнений.
Пример запроса: POST /solve_equations/
    {
        "equations": ["x+y=1", "x-y=3"]
    }
    


class StatRequest(BaseModel):
    numbers: list
    stat_type: str

@app.post("/statistic/")


Вычисляет статистику по заданному типу.
Пример запроса: POST /statistic/
    {
        "numbers": [1, 2, 3, 4],
        "stat_type": "mean"
    }

Доступные виды stat_type: "mean", "median", "max", "min", "range", "variance"(Среднее значение, медиана, максимум, мимнимум, размах, дисперсия)

class FracRequest(BaseModel):
    first: str
    second: str
    oper: str

@app.post("/fractions/")


Производит арифметические операции с дробями.
Пример запроса: POST /fractions/
    {
        "first": "1/2",
        "second": "1/3",
        "oper": "+"
    }
Доступные oper: + - * /

class TrigRequest(BaseModel):
    number: str
    type: str

@app.post("/trigonometry/")
Вычисляет тригонометрическую функцию.
Пример запроса: POST /trigonometry/
    {
        "number": "30",
        "type": "sin"
    }
Доступны type: "sin", "cos", "tan", "ctg", "arcsin", "arccos", "arctan".
class SchisOPRequest(BaseModel):
    first: str
    second: str
    oper: str
    ss: str

@app.post("/schislen/operations/")
Проводит операции перевода в разные системы счисления.
Пример запроса: POST /schislen/operations
    {
        "first": "10",
        "second": "2",
        "oper": "+",
        "ss": "10"
    }
    """
2<ss<36
class SchisPerRequest(BaseModel):
    num: str
    ss1: str
    ss2: str


@app.post("/schislen/perevod/")


Осуществляет перевод числа из одной системы счисления в другую.
Пример запроса: POST /schislen/perevod
    {
        "num": "1010",
        "ss1": "2",
        "ss2": "10"
    }
