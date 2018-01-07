class Recursion(object):
	"""docstring for Recursion"""
	def listsum(numList):
		theSum = 0
		for i in numList:
			theSum += i
		return theSum

	print(listsum([1,3,5,6,9]))