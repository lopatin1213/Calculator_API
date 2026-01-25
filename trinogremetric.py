import addings
import math
from sympy import *

def process_trigonometric_function(number, function_type):
	"""Вычисляет тригонометрическую функцию указанного типа."""
	try:
		angle = float(number)
		radians = math.radians(angle)
		if function_type == 'sin':
			result = math.sin(radians)
		elif function_type == 'cos':
			result = math.cos(radians)
		elif function_type == 'tan':
			result = math.tan(radians)
		elif function_type == 'arcsin':
			result = math.degrees(math.asin(math.degrees(radians)))
		elif function_type == 'arccos':
			result = math.degrees(math.acos(math.degrees(radians)))
		elif function_type == 'arctan':
			result = math.degrees(math.atan(math.degrees(radians)))
		
		else:
			raise ValueError(f'Неверный тип тригонометрической функции: {function_type}')
		final_result = addings.format_number(addings.dynamic_precision(result))
		return final_result
		
	except ValueError as ve:
		return str(ve)
	except Exception as e:
		return str(e)