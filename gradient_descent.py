import math
import numpy as np
def gradient_descent(f, x, n):
	prev_x = 0
	while (True):
		prev_x = x
		g = f(x)
		x = x - n*g
		if (magnitude(x) < 0.0001): # the steps become very small
			break;
	return x

def magnitude(x):
	y = 0;
	for i in x:
		y = y + i*i
	return math.sqrt(y)
	