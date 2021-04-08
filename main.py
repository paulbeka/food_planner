import random, csv, os
from food_planner.meal import Meal
from food_planner.foodItem import FoodItem


BASE_DIR = os.getcwd()
MEAL_LOC = os.path.join("data", "meals.csv")
ITEM_LOC = os.path.join("data", "cupboard.csv")
PRICE_LOC = os.path.join("data", "prices.csv")
DATA_LOC = os.path.join("data", "data.txt")


def getMeals():
	meals = []
	with open(os.path.join(BASE_DIR, MEAL_LOC), "r") as file:
		csv_reader = csv.reader(file, delimiter=',')
		for row in csv_reader:
			meals.append(Meal(row[0], row[1:]))
	return meals


def getItems(loc):
	items = []
	with open(os.path.join(BASE_DIR, loc), "r") as file:
		csv_reader = csv.reader(file, delimiter=',')
		for row in csv_reader:
			items.append(FoodItem(row[0], row[1], row[2]))
	return items


def loadData():
	with open(os.path.join(BASE_DIR, DATA_LOC), "r") as f:
		return f.readlines()


def addMeal(name, ingredients):
	with open(os.path.join(BASE_DIR, MEAL_LOC), "r+") as file:
		csv_reader = csv.reader(file, delimiter=",")
		for row in csv_reader:
			if row[0] == name:
				print("[ FAIL ] Meal already exists")
				return
		items = ""
		for i in ingredients:
			items += f"{i.name}:{i.quantity}" + ","
		file.write(f"{name},{items[:-1]}\n")
	

def addFoodItem(name, quantity):
	with open(os.path.join(BASE_DIR, ITEM_LOC), "a") as file:
		file.write(f"{name},{str(quantity)},{str(price)}\n")

def editFoodItem(name, quantity)


def addPriceItem(name, quantity, price):
	with open(os.path.join(BASE_DIR,PRICE_LOC),"r+") as file:
		for row in csv.reader(file, delimiter=","):
			if row[0] == name:
				print("[ FAIL ] Price is already added")
				return
		file.write(f"{name},{str(quantity)},{str(price)}\n")


def main():

	balance = getData()

	items = getItems(ITEM_LOC)
	prices = getItems(PRICE_LOC)
	meals = getMeals()

	print("ITEMS:")

	print(meals[0].ingredients)
	print(str(items[0]))

if __name__ == "__main__":
	main()