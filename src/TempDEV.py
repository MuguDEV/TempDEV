# Temperature Conversion
# Available SCALES OF TEMPERTURE

# * CELSIUS SCALE
# * FARENHEIT SCALE
# * KELVIN SCALE
# * RANKINE SCALE
# * DELISLE SCALE

# These Converions are based on these Internet resources 

# * https://en.wikipedia.org/wiki/Conversion_of_scales_of_temperature
# * https://www.google.com/search?q=Temperature+Converter 

import json

class Temperature_Converions:

	def __convert(dic :dict, return_type):
		if return_type == 'l':
			return list(dic.items())
		elif return_type == 't':
			return tuple(list(dic.items()))
		elif return_type  == 's':
			return set(list(dic.items()))
		elif return_type == 'd':
			return dic
		elif return_type == 'j':
			return json.dumps(dic, indent=2)
		else:
			return f"ReturnTypeError: Unknown Return_Type ==> {return_type}"


	def convert(self, scale :str ='c',value :int = 1, return_type :str = 'd'):
		if scale == 'c':
			dic = {
				'Fahrenheit' : (value * 9/5) + 32,
				'Kelvin' : value + 273.15,
				'Rankine' : value * 9/5 + 491.67,
				'Delisle' : (100 - value) * 3/2
				}
			return Temperature_Converions.__convert(dic, return_type)
		elif scale == 'f':
			dic = {
				'Celsius' : (value - 32) * 5/9,
				'Kelvin' : (value - 32) * 5/9 + 273.15,
				'Rankine' : value + 459.67,
				'Delisle' : (212 - value) * 5/6
				}
			return Temperature_Converions.__convert(dic, return_type)
		elif scale == 'k':
			dic = {
				'Celsius' : value - 273.15,
				'Fahrenheit' : (value - 273.15) * 9/5 + 32,
				'Rankine' : value * 1.8,
				'Delisle' : (373.15 - value) * 3/2
				}
			return Temperature_Converions.__convert(dic, return_type)
		elif scale == 'r':
			dic = {
				'Celsius' : (value - 491.67) * 5/9,
				'Fahrenheit' : value - 459.67,
				'Kelvin' : value * 5/9,
				'Delisle' : (671.67 - value) * 5/6
				}
			return Temperature_Converions.__convert(dic, return_type)
		elif scale == 'd':
			dic = {
				'Celsius' : 100 - value * 2/3 ,
				'Fahrenheit' : 212 - value * 6/5,
				'Kelvin' : 373.15 - (value * 2/3),
				'Rankine' : 671.67 - value * 6/5
				}
			return Temperature_Converions.__convert(dic, return_type)
		else:
			return f"ScaleError: Unknown Scale ==> {scale}"

	def symbols(self, scale):
		if scale == 'c':
			return '°C'
		elif scale == 'f':
			return '°F'
		elif scale == 'k':
			return 'K'
		elif scale == 'r':
			return '°R'
		elif scale == 'd':
			return '°De'
		else:
			return f"ScaleError: Unknown Scale ==> {scale}"
