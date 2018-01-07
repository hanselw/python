import time

def sumOfN2(n):
	start = time.time()

	theSum = 0
	for i in range(1, n+1):
		theSum += i

	end = time.time()

	return theSum, end-start

def foo(tom):
	fred = 0
	for bill in range(1,tom+1):
		barney = bill  
		fred += barney

	return fred

#print(foo(2))

for i in range(5):
	print("Sum is %d required %10.7f seconds"%sumOfN2(1000000))

def anagramSolution1(s1,s2):
