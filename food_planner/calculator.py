import random
from food_planner.tools import getMeals, getItems, updateCupboard

POOR, MEDIUM, RICH = 2, 3, 5

class Calculator:

	def __init__(self, budget, time):
		self.meals = getMeals()
		self.cupboard = getItems()
		if time < 1:
			raise Exception("Time must be above 0.")
		if budget < 1:
			raise Exception("Budget must be above 1.")
		self.budget = budget
		self.time = time


	# Run the program depending on the mode
	def run(self, mode):
		if mode:
			return self.calculate(True)
		else:
			meal_plan = self.calculate(False)
			updateCupboard(self.cupboard)
			return meal_plan


	# Calculate a meal plan or shopping list
	def calculate(self, shopping):

		# The final return list
		meal_plan = []

		rich_meals = []
		medium_meals = []
		poor_meals = []

		# meals that have already been selected and don't want to be selected
		# several times in a row.
		cached_meals = []

		# classify meal prices
		for meal in self.meals:
			if meal.price > 5:
				rich_meals.append(meal)
			elif meal.price >= 3:
				medium_meals.append(meal)
			else:
				poor_meals.append(meal)

		# For every block of days select some random meals and appends

		for i in range(self.time):
			dailyBudget = self.budget / self.time

			# Check what meals you can cook 
			if not shopping:
				poor_meals = self.getPossibleMeals(poor_meals)
				medium_meals = self.getPossibleMeals(medium_meals)
				rich_meals = self.getPossibleMeals(rich_meals)
				self.meals = self.getPossibleMeals(self.meals)

			# Get attraction values
			poorAttraction = (RICH - dailyBudget) * 10
			richAttraction = dailyBudget * 10
			mediumAttraction = MEDIUM*10 + (richAttraction - poorAttraction)

			threshold = (100-int(poorAttraction)) + int(richAttraction)
			r = random.randint(0, threshold)
			# In the rich range
			if r > (50 + int(mediumAttraction/3)) and len(rich_meals) != 0:
				meal_plan.append(random.choice(rich_meals))
			# In the poor range
			elif r < (50-int(mediumAttraction/3)) and len(poor_meals) != 0:
				meal_plan.append(random.choice(poor_meals))
			else:
				if len(medium_meals) != 0:
					meal_plan.append(random.choice(medium_meals))
				else:
					if len(self.meals) == 0:
						print("Cannot calculate a meal path.")
						return
					meal_plan.append(random.choice(self.meals))

			# Update the budget and the ingredient quantities
			self.budget -= meal_plan[-1].price
			if not shopping:
				for ingredient in meal_plan[-1].ingredients:
					self.cupboard[ingredient.name].quantity -= ingredient.quantity


			if self.budget <= 0:
				return

		return meal_plan


	def generateShoppingList(self):
		pass


	# Get a list of possible meals with items in the cupboard
	def getPossibleMeals(self, meals):
		final = []
		for meal in meals:
			if meal.checkCanCook(self.cupboard):
				final.append(meal)

		return final
