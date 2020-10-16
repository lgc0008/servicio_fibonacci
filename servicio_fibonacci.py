
def fib():
	x, y = 0, 1
	while 1:
		yield x
		x, y = y, x + y


def fibonacci(fib_largo):
	if fib_largo < 1:
		raise ValueError("Entrada no valida. Ingrese valor mayor a cero") 
	series = []
	x = fib()
	for i in range(fib_largo):
		series.append(x.next())
	return series