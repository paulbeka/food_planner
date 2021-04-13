class Meal:

	def __init__(self, name, ingredients):
		self.name = name
		self.ingredients = ingredients
		self.price = self.calcPrice()

	def __str__(self):
		return self.name + ", ingredients: " + str(self.ingredients)

	# Calculate your own price
	def calcPrice(self):
		price = 0

		for ingredient in self.ingredients:
			price += ingredient.price * ingredient.quantity

		return price
