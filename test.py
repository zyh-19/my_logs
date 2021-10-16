class C2:
	z = 'wc2x'
	def __init__(self,a) -> None:
		self.x = 'C2x'
		self.z = a

class C3:
	def __init__(self) -> None:
		self.w = 'C3w'
		self.z = 'C3w'

class C1(C2,C3):
	def __init__(self) -> None:
		self.x = 'Cx1'
		self.y = 'C1y'
		print(self.z)

I1 = C1()
I2 = I1
print(I1 == I2)

# class C2:
# 	x = 'C2x'
# 	z = 'C2z'

# class C3:
# 	w = 'C3w'
# 	z = 'C3w'

# class C1(C2,C3):
# 	x = 'C1x'
# 	y = 'C1y'

# I1 = C1()
# I2 = C1()
# print(C1.x)