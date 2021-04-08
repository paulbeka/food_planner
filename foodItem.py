class FoodItem:

	def __init__(self, name, buyQuantity, price):
		self.name = name
		self.quantity = buyQuantity
		self.price = price

	def __str__(self):
		return "[" + self.name + "," + str(self.quantity) + "," + str(self.price) + "]"