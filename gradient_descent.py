import math
def gradient_descent(f, x, n):
	g = f(x)
	while magnitude(g) > 0.0001:
		x = x - n*g
		g = f(x)
	return x

def magnitude(x):
	y = 0;
	for i in x:
		y = y + i*i
	return math.sqrt(y)
