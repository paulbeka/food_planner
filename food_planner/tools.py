import csv, os
from food_planner.meal import Meal
from food_planner.foodItem import FoodItem
from food_planner.settings import BASE_DIR, ITEM_LOC, MEAL_LOC

# Load meal data from meals.csv
def getMeals():
	meals = []
	with open(os.path.join(BASE_DIR, MEAL_LOC), "r") as file:
		csv_reader = csv.reader(file, delimiter=',')
		for row in csv_reader:
			items = []
			for ingredient in row[1:]:
				items.append(ingredient.split(":"))
			ingredients = [FoodItem(item[0], item[1], item[2]) for item in items]
			# TODO: fix bug where not all ingredients are loaded
			meals.append(Meal(row[0], ingredients))
	return meals


# Load the cupboard items
def getItems():
	items = {}
	with open(os.path.join(BASE_DIR, ITEM_LOC), "r") as file:
		csv_reader = csv.reader(file, delimiter=',')
		for row in csv_reader:
			items[row[0]] = FoodItem(row[0], row[1], row[2])
	return items


# Load all user data
def loadData():
	with open(os.path.join(BASE_DIR, DATA_LOC), "r") as f:
		return f.readlines()


# Add a meal to all the meals
def updateMeal(meals):
	with open(os.path.join(BASE_DIR, MEAL_LOC), "w") as file:
		for meal in meals:
			items = ""
			for i in meal.ingredients:
				items += f'{i.name}:{i.quantity}:{i.price},'
			file.write(f"{meal.name},{items[:-1]}\n")
		

# Add an item that you can shop
def updateCupboard(items):
	# Fix the population list script
	with open(os.path.join(BASE_DIR, ITEM_LOC), "w") as f:
		for name in items.keys():
			f.write(f"{name},{str(items[name].quantity)},{str(items[name].price)}\n")