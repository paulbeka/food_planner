import random, csv, os
from food_planner.meal import Meal
from food_planner.foodItem import FoodItem
from food_planner.tools import getItems, getMeals


POOR, MEDIUM, RICH = 2, 3, 5


def calculateMealPlan(budget, time, meals):

	# check that meals can be calculated
	if time < 1 or budget < 1 or meals == []:
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
		print(meal.price)
		if meal.price > 5:
			rich_meals.append(meal)
		elif meal.price >= 3:
			medium_meals.append(meal)
		else:
			poor_meals.append(meal)

	print(rich_meals)
	print(medium_meals)
	print(poor_meals)

	# For every block of days select some random meals and appends

	for i in range(time):
		dailyBudget = budget / time

		poorAttraction = (RICH - dailyBudget) * 10
		richAttraction = dailyBudget * 10
		mediumAttraction = MEDIUM*10 + (richAttraction - poorAttraction)

		threshold = (100-int(poorAttraction)) + int(richAttraction)
		r = random.randint(0, threshold)
		if r > (50 + int(mediumAttraction/3)) and len(rich_meals) != 0:
			meal_plan.append(rich_meals[random.randint(0,len(rich_meals)-1)])
		elif r < (50-int(mediumAttraction/3)) and len(poor_meals) != 0:
			meal_plan.append(poor_meals[random.randint(0,len(poor_meals)-1)])
		else:
			if len(medium_meals) != 0:
				meal_plan.append(medium_meals[random.randint(0,len(medium_meals)-1)])
			else:
				meal_plan.append(meals[random.randint(0,len(meals)-1)])

		budget -= meal_plan[-1].price

		if budget <= 0:
			return


	return meal_plan

def main():

	# balance = getData()

	items = getItems()
	meals = getMeals()

	budget = 100
	time = 10

	for item in calculateMealPlan(budget, time, meals):
		items[item.name] = 0


if __name__ == "__main__":
	main()