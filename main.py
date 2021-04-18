import random, csv, os, sys
from food_planner.meal import Meal
from food_planner.foodItem import FoodItem
from food_planner.tools import getItems, getMeals, updateCupboard
from food_planner.dataAdder import DataAdder


POOR, MEDIUM, RICH = 2, 3, 5


def checkCanCook(meal, cupboard):
	for ingredient in meal.ingredients:
		if ingredient != None and ingredient.name in cupboard.keys():
			#print(cupboard[ingredient.name].quantity, ingredient.quantity)
			if cupboard[ingredient.name].quantity < ingredient.quantity:
				return False
	return True


def calculateMealPlan(budget, time, meals, cupboard):

	# check that meals can be calculated
	if time < 1 or budget < 1 or meals == []:
		print("The meal list, budget, or time was too low.")
		return

	# The final return list
	meal_plan = []

	rich_meals = []
	medium_meals = []
	poor_meals = []

	# meals that have already been selected and don't want to be selected
	# several times in a row.
	cached_meals = []

	# classify meal prices
	for meal in meals:
		if meal.price > 5:
			rich_meals.append(meal)
		elif meal.price >= 3:
			medium_meals.append(meal)
		else:
			poor_meals.append(meal)

	# For every block of days select some random meals and appends

	for i in range(time):
		dailyBudget = budget / time

		# Check what meals you can cook
		poor_meals = getPossibleMeals(poor_meals, cupboard)
		medium_meals = getPossibleMeals(medium_meals, cupboard)
		rich_meals = getPossibleMeals(rich_meals, cupboard)
		meals = getPossibleMeals(meals, cupboard)

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
				if len(meals) == 0:
					print("Cannot calculate a meal path.")
					return
				meal_plan.append(random.choice(meals))
		# Update the budget and the ingredient quantities
		budget -= meal_plan[-1].price
		for ingredient in meal_plan[-1].ingredients:
			cupboard[ingredient.name].quantity -= ingredient.quantity

		if budget <= 0:
			return

	return meal_plan


def getPossibleMeals(meals, cupboard):
	final = []
	for meal in meals:
		if checkCanCook(meal, cupboard):
			final.append(meal)

	return final


def runCalculator():
	items = getItems()
	meals = getPossibleMeals(getMeals(), items)

	# No meals can be made with what is in the cupboard
	if meals == None or meals == []:
		print("No possible meals.")
		return

	budget = 100
	time = 10

	meal_plan = calculateMealPlan(budget, time, meals, items)
	if meal_plan == None:
		print("No meal plan can be calculated.")
	
	# Remove amound of ingredients needed
	for item in meal_plan:
		print(item)

	updateCupboard(items)	


def main():

	DataAdder().run()
	runCalculator()
	

if __name__ == "__main__":
	main()