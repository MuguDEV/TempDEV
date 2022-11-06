# Temperature Conversion
# Available SCALES OF TEMPERTURE

# * CELSIUS SCALE
# * FARENHEIT SCALE
# * KELVIN SCALE

# These Converions are based on these Internet resources 

# * https://en.wikipedia.org/wiki/Conversion_of_scales_of_temperature
# * https://www.google.com/search?q=Temperature+Converter 


# Class for Celsius Scale
class Celsius:
	values = {}

	def convert(self, value):
		Celsius.values = {
		'Fahrenheit' : (value * 9/5) + 32,
		'Kelvin' : value + 273.15 
		}
		return Celsius.values

# Class for Farenheit Scale
class Fahrenheit:
	values = {}
	
	def convert(self, value):
		Fahrenheit.values = {
		'Celsius' : (value - 32) * 5/9,
		'Kelvin' : (value - 32) * 5/9 + 273.15
		}
		return Fahrenheit.values

# Class for Kelvin Scale
class Kelvin:
	values = {}

	def convert(self, value):
		Kelvin.values = {
		'Celsius' : value - 273.15,
		'Fahrenheit' : (value - 273.15) * 9/5 + 32 
		}
		return Kelvin.values