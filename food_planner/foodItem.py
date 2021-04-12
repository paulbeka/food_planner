class FoodItem:

	def __init__(self, name, quantity, price):
		self.name = name
		self.quantity = float(quantity)
		self.price = float(price)

	def __str__(self):
		return self.name + "," + str(self.quantity) + "," + str(self.price)