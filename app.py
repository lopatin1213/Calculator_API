from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
import ast
from calculate import calculate_1, arithmetic_operation_fractions
from equations import solve_system_of_equations
from statistic import calculate_statistics
from pydantic import BaseModel
from trinogremetric import process_trigonometric_function
from schislen import calculate_sch, perevod_to
import logging

# Настроим логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
class CalcRequests(BaseModel):
    expr: str
@app.post("/calculate/")
async def calculate(req: CalcRequests):
    """
    Вычисляет простое арифметическое выражение, переданное в GET-запросе.
    Пример запроса: GET /calculate/?expr=2+2
    """
    logger.info(f"Calculate requested with expr: {req.expr}")
    result = calculate_1(req.expr)
    return JSONResponse(content={"result": result})
class EquationsRequests(BaseModel):
    equations: str
@app.post("/solve_equations/")
async def solve_equations(req: EquationsRequests):
    """
    Решает систему уравнений.
    Пример запроса: POST /solve_equations/
    {
        "equations": ["x+y=1", "x-y=3"]
    }
    """
    logger.info(f"Solve equations requested with equations: {req.equations}")
    result = solve_system_of_equations(req.equations)
    return JSONResponse(content={"result": result})

class StatRequest(BaseModel):
    numbers: list
    stat_type: str

@app.post("/statistic/")
async def stat(req: StatRequest):
    """
    Вычисляет статистику по заданному типу.
    Пример запроса: POST /statistic/
    {
        "numbers": [1, 2, 3, 4],
        "stat_type": "mean"
    }
    """
    logger.info(f"Statistic requested with numbers: {req.numbers}, stat_type: {req.stat_type}")
    result = calculate_statistics(req.numbers, req.stat_type)
    return JSONResponse(content={"result": result})

class FracRequest(BaseModel):
    first: str
    second: str
    oper: str

@app.post("/fractions/")
async def frac(req: FracRequest):
    """
    Производит арифметические операции с дробями.
    Пример запроса: POST /fractions/
    {
        "first": "1/2",
        "second": "1/3",
        "oper": "+"
    }
    """
    logger.info(f"Fractions requested with first: {req.first}, second: {req.second}, oper: {req.oper}")
    result = arithmetic_operation_fractions(req.first, req.second, req.oper)
    return JSONResponse(content={"result": str(result)})

class TrigRequest(BaseModel):
    number: str
    type: str

@app.post("/trigonometry/")
async def trig(req: TrigRequest):
    """
    Вычисляет тригонометрическую функцию.
    Пример запроса: POST /trigonometry/
    {
        "number": "30",
        "type": "sin"
    }
    """
    logger.info(f"Trigonometry requested with number: {req.number}, type: {req.type}")
    result = process_trigonometric_function(req.number, req.type)
    return JSONResponse(content={"result": result})

class SchisOPRequest(BaseModel):
    first: str
    second: str
    oper: str
    ss: str

@app.post("/schislen/operations/")
async def schis_op(req: SchisOPRequest):
    """
    Проводит операции перевода в разные системы счисления.
    Пример запроса: POST /schislen/operations
    {
        "first": "10",
        "second": "2",
        "oper": "+",
        "ss": "10"
    }
    """
    logger.info(f"Schislen operations requested with first: {req.first}, second: {req.second}, oper: {req.oper}, ss: {req.ss}")
    result = calculate_sch(req.first, req.second, req.oper, req.ss)
    return JSONResponse(content={"result": result})

class SchisPerRequest(BaseModel):
    num: str
    ss1: str
    ss2: str

@app.post("/schislen/perevod/")
async def schis_per(req: SchisPerRequest):
    """
    Осуществляет перевод числа из одной системы счисления в другую.
    Пример запроса: POST /schislen/perevod
    {
        "num": "1010",
        "ss1": "2",
        "ss2": "10"
    }
    """
    logger.info(f"Schislen perevod requested with num: {req.num}, ss1: {req.ss1}, ss2: {req.ss2}")
    result = perevod_to(req.num, req.ss1, req.ss2)
    return JSONResponse(content={"result": result})