import random, csv, os
from food_planner.meal import Meal
from food_planner.foodItem import FoodItem


BASE_DIR = os.getcwd()
MEAL_LOC = os.path.join("data", "meals.csv")
ITEM_LOC = os.path.join("data", "cupboard.csv")
PRICE_LOC = os.path.join("data", "prices.csv")
DATA_LOC = os.path.join("data", "data.txt")


# Load meal data from meals.csv
def getMeals():
	meals = {}
	with open(os.path.join(BASE_DIR, MEAL_LOC), "r") as file:
		csv_reader = csv.reader(file, delimiter=',')
		for row in csv_reader:
			meals[row[0]] = Meal(row[0], row[1:])
	return meals


# Load the cupboard items
def getItems(loc):
	items = {}
	with open(os.path.join(BASE_DIR, loc), "r") as file:
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
				items += f"{i.name}:{i.quantity}" + ","
			file.write(f"{meal.name},{items[:-1]}\n")
		

# Add an item that you can shop
def updateCupboard(items):
	with open(os.path.join(BASE_DIR, ITEM_LOC), "w") as f:
		for item in items:
			print(f"Adding {item.name}")
			f.write(f"{item.name},{str(item.quantity)},{str(item.price)}\n")


# Write item prices to the files
def updatePriceItem(prices):
	with open(os.path.join(BASE_DIR, PRICE_LOC),"w") as file:
		for price in prices:
			file.write(f"{price.name},{str(price.quantity)},{str(price.price)}\n")


def calculateMealPlan(budget, time):
	time *= 2


def main():

	# balance = getData()

	items = getItems(ITEM_LOC)
	prices = getItems(PRICE_LOC)
	meals = getMeals()

	budget = float(input("Enter amount of money: "))
	time = int(input("Enter number of days: "))


if __name__ == "__main__":
	main()