
import addings

import logging
def variance(numbers):
	"""Вычисляет дисперсию списка чисел."""
	mean = sum(numbers) / len(numbers)
	squared_diffs = [(num - mean) ** 2 for num in numbers]
	return sum(squared_diffs) / len(numbers)


def calculate_statistics(numbers, stat_type):
	"""Вычисляет статистику набора чисел (среднее, медиана, минимум, максимум, размах, дисперсия)."""
	
	try:
		
		
		logging.info(numbers)
		if not numbers:
			return None
		if stat_type == "mean":
			mean = sum(numbers) / len(numbers)
			final_result = addings.dynamic_precision(mean)
			return final_result
		elif stat_type == "median":
			sorted_numbers = sorted(numbers)
			mid = len(sorted_numbers) // 2
			median = (sorted_numbers[mid] + sorted_numbers[-mid - 1]) / 2 if len(sorted_numbers) % 2 == 0 else \
				sorted_numbers[mid]
			final_result = addings.dynamic_precision(median)
			return final_result
		elif stat_type == "max":
			maximum = max(numbers)
			final_result = addings.dynamic_precision(maximum)
			
			return final_result
		elif stat_type == "min":
			minimum = min(numbers)
			final_result = addings.dynamic_precision(minimum)
			
			return final_result
		elif stat_type == "range":
			rng = max(numbers) - min(numbers)
			final_result = addings.dynamic_precision(rng)
			
			return final_result
		elif stat_type == "variance":
			var = variance(numbers)
			final_result = addings.dynamic_precision(var)
			
			return final_result
		else:
			raise ValueError(f"Неподдерживаемый тип статистики: {stat_type}")
		
		
		
		
	except ValueError as ve:
		return str(ve)
	except Exception as e:
		return str(e)

