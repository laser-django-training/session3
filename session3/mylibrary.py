def iseven(x):
	try:
		return x % 2 == 0
	except:
		return False

def isodd(x):
	return not iseven(x)
