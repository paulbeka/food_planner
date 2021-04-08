import random, json, os
from food_planner.meal import Meal
from food_planner.foodItem import FoodItem


BASE_DIR = os.getcwd()
MEAL_LOC = os.path.join("data", "meals.json")
ITEM_LOC = os.path.join("data", "cupboard.json")


def getMeals():
	with open(os.path.join(BASE_DIR, MEAL_LOC), "r") as file:
		data = json.load(file)

	items = []
	for meal in data["meals"]:
		items.append(Meal(meal["name"], meal["ingredients"]))
	return items

def getFoodItems():
	with open(os.path.join(BASE_DIR, ITEM_LOC), "r+") as file:
		data = json.load(file)

	items = []
	for item in data["items"]:
		items.append(FoodItem(item["name"], item["quantity"], item["price"]))


def addMeal(name, ingredients):
	with open(os.path.join(BASE_DIR, MEAL_LOC), "r+") as file:
		data = json.loads(file)
		data["meals"].append(Meal(name, ingredients))
		json.dumps(data, file)
	

def addFoodItem(name, price, quantity):
	with open(os.path.join(BASE_DIR, ITEM_LOC), "r+") as file:
		data = json.loads(file)
		data["items"].append(FoodItem(name, price,quantity))
		json.dumps(data, file)


def main():


	
	meals = getMeals()
	items = getFoodItems()

