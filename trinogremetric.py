import addings
import math
from sympy import *
import logging
def process_trigonometric_function(num, function_type):
	"""Вычисляет тригонометрическую функцию указанного типа."""
	try:
		angle = float(num)
		radians = math.radians(angle)
		if function_type == 'sin':
			result = math.sin(radians)
		elif function_type == 'cos':
			result = math.cos(radians)
		elif function_type == 'tan':
			result = math.tan(radians)
		elif function_type == 'ctg':
			result = math.cos(radians) / math.sin(radians)
		elif function_type == 'arcsin':
			result = math.degrees(math.asin(math.degrees(radians)))
		elif function_type == 'arccos':
			result = math.degrees(math.acos(math.degrees(radians)))
		elif function_type == 'arctan':
			result = math.degrees(math.atan(math.degrees(radians)))
		else:
			raise ValueError(f'Неверный тип тригонометрической функции: {function_type}')
		final_result = addings.format_number(addings.dynamic_precision(result))
		
		return str(final_result)
	except ValueError as ve:
		logging.error(str(ve))
		return str(ve)
	except Exception as e:
		return str(e)
		