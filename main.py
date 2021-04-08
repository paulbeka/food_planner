import random, csv, os
from food_planner.meal import Meal
from food_planner.foodItem import FoodItem


BASE_DIR = os.getcwd()
MEAL_LOC = os.path.join("data", "meals.csv")
ITEM_LOC = os.path.join("data", "cupboard.csv")


def getMeals():
	meals = []
	with open(os.path.join(BASE_DIR, MEAL_LOC), "r") as file:
		csv_reader = csv.reader(file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			meals.append(Meal(row[0], row[1:]))
	return meals


def getFoodItems():
	items = []
	with open(os.path.join(BASE_DIR, ITEM_LOC), "r") as file:
		csv_reader = csv.reader(file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			items.append(FoodItem(row[0], row[1], row[2]))
	return items

def addMeal(name, ingredients):
	with open(os.path.join(BASE_DIR, MEAL_LOC), "a") as file:
		items = []
		for i in ingredients:
			items.append(f"[{i.name}:{i.quantity}]")
		file.write(f"{name},{str(items)}")
	

def addFoodItem(name, price, quantity):
	with open(os.path.join(BASE_DIR, ITEM_LOC), "a") as file:
		file.write(f"{name},{str(quantity)},{str(price)}")


def main():

	#addFoodItem("chicken", 200.0, 2)
	
	items = getFoodItems()

	addMeal("chicken", [items[0]])

	meals = getMeals()

	print("ITEMS:")

	print(meals[0].ingredients)
	print(str(items[0]))

if __name__ == "__main__":
	main()