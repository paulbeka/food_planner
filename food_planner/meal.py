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


	# return whether or not you can cook this meal given the amount of food in the cupboard
	def checkCanCook(self, cupboard):
		for ingredient in self.ingredients:
			if ingredient != None and ingredient.name in cupboard.keys():
				if cupboard[ingredient.name].quantity < ingredient.quantity:
					return False
		return True


	# Return list of ingredients not in the cupboard that are needed
	def findIngredientsNeeded(self, cupboard):
		needed = []
		for ingredient in self.ingredients:
			if ingredient == None:
				continue
			if ingredient.name in cupboard.keys():
				if cupboard[ingredient.name].quantity < ingredient.quantity:
					needed.append([ingredient.name, ingredient.quantity - cupboard[ingredient.name].quantity])
			else:
				needed.append([ingredient.name, ingredient.quantity])

		return needed
