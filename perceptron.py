import numpy as np
def AND(x1, x2):
	x = np.array([x1, x2])
	w = np.array([0.5, 0.5])
	b = -0.7
	out = np.sum(w*x) + b
	if out <= 0:
		return 0
	else:
		return 1

def NAND(x1, x2):
	x = np.array([x1, x2])
	w = np.array([-0.5, -0.5])
	b = 0.7
	out = np.sum(w*x) + b
	if out <= 0:
		return 0
	else:
		return 1

def OR(x1, x2):
	x = np.array([x1, x2])
	w = np.array([0.5, 0.5])
	b = -0.1
	out = np.sum(w*x) + b
	if out <= 0:
		return 0
	else:
		return 1

def XOR(x1, x2):
	s1 = NAND(x1, x2)
	s2 = OR(x1, x2)
	out = AND(s1, s2)
	return out

print (XOR(0, 0))
print (XOR(0, 1))
print (XOR(1, 0))
print (XOR(1, 1))