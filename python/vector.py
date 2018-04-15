class Vector:
	def __init__(self,cordinates):
		self.cordinates = tuple(cordinates);
		self.dimension = len(cordinates);
	
	def __str__(self):
		return "Vector : {}".format(self.cordinates);
		
	def __eq__(self,v):
		return self.cordinates==v.cordinates;
	def __add__(self,v):
		arr = []
		for i in range(len(v.cordinates)):
			arr.append(v.cordinates[i]+self.cordinates[i])
		return Vector(arr);
	def __sub__(self,v):
		arr = []
		for i in range(len(v.cordinates)):
			arr.append(v.cordinates[i]-self.cordinates[i])
		return Vector(arr);
	def __mul__(self,v):
		arr = []
		for i in range(len(self.cordinates)):
			arr.append(v*self.cordinates[i])
		return Vector(arr);
v =  Vector([1,2,3]);
v1 = Vector([1,2,3]);
print v1*2