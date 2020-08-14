def mysqrt(a):
	epsilon = 0.00001
	x = 10
	while True:
		y = (x + a/x) / 2
		if abs(y - x) < epsilon:
			return y
			break
		x = y
		
from math import sqrt

def test_square_root():
	print("a   mysqrt(a)     math.sqrt(a)  diff")
	print("-   ---------     ------------	----")
	for a in range(1, 10):
		print("{:.1f} {:.11f} {:.11f} {}".format(a,mysqrt(a), sqrt(a), mysqrt(a)-sqrt(a)))
		
test_square_root()