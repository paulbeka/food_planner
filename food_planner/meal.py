class Meal:

	def __init__(self, name, ingredients):
		self.name = name
		self.ingredients = ingredients

	def __str__(self):
		return self.name + ", ingredients: " + str(self.ingredients)

	def calcPrice(self):
		price = 0

		for ingredient in self.ingredients:
			price += ingredient.price * ingredient.quantity

		return price
