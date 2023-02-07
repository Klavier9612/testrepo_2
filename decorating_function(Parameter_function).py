def decorating_function(Parameter_function):

	def internal_function(*args, **kwargs):	

		print("An operation will be done")

		Parameter_function(*args, **kwargs)

		print("The operation has been done")

	return internal_function


@decorating_function
def sum(num1,num2):

	print(num1+num2)

def substraction(num1,num2):

	print(num1-num2)

@decorating_function
def potencia(base,exponent):

	print(pow(base,exponent))

sum(1,1)
substraction (4,2)

potencia(base=5, exponent=3)