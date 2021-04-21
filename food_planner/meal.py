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

	def checkCanCook(self, cupboard):
		for ingredient in self.ingredients:
			if ingredient != None and ingredient.name in cupboard.keys():
				if cupboard[ingredient.name].quantity < ingredient.quantity:
					return False
		return True
