import os, csv
from food_planner.foodItem import FoodItem
from food_planner.meal import Meal
from food_planner.tools import getPrices, getMeals, updateMeals, updatePrices

class DataAdder:

	def __init__(self):
		self.priceList = getPrices()
		self.exit = False


	def addPrices(self):
		
		# Loop until input is "###"
		while True:
			item_name = input("Name: ")

			if item_name == "###":
				print("Exiting.")
				break

			item_price = float(input("Price: "))
			item_quantity = float(input("Quantity: "))

			self.priceList[item_name] = FoodItem(item_name, item_price, item_price/item_quantity)

		updatePrices(self.priceList)

	def addMeals(self):

		meals_to_add = []

		while True:
			meal_name = input("Name: ")

			if meal_name == "###":
				print("Exiting.")
				break

			ingredients = []

			while True:
				ingredient_name = input("Ingredient name: ")

				ingredient_price = 0
				for price in self.priceList:
					if price.name == ingredient_name:
						ingredient_price = price.price
						break

				if ingredient_price == 0:
					print("Item not found. Please try again.")
					continue

				if ingredient_name == "###" and not ingredients:
					meals_to_add.append(Meal(meal_name, ingredients))
					print("Meal has been added.")
					break

				ingredient_quantity = float(input("Ingredient quantity: "))

				ingredients.append(FoodItem(ingredient_name, ingredient_quantity, ingredient_price))
				print("Ingredient has been added.")

		meals = getMeals() + meals_to_add
		updateMeals(meals)


	def run(self):

		while not self.exit:

			choice = input("Add prices or meals or quit (p/m/q): ")
			if choice == "p":
				self.addPrices()
			elif choice == "m":
				self.addMeals()
			else:
				self.exit = True

		print("Exiting data adder.")

