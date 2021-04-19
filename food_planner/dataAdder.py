import os, csv
from food_planner.foodItem import FoodItem
from food_planner.meal import Meal
import food_planner.tools as tools	

# TODO: check that price or meal does not already exist.

class DataAdder:

	def __init__(self):
		self.priceList = tools.getPrices()
		self.exit = False


	def addPrices(self):
		
		# Loop until input is "###"
		while True:
			item_name = input("Name: ")

			if item_name == "###":
				print("Exiting.")
				break

			if item_name in self.priceList.keys():
				print("Item already exists. Enter new item.")
				continue

			item_price = float(input("Price: "))
			item_quantity = float(input("Quantity: "))

			self.priceList[item_name] = FoodItem(item_name, item_quantity, item_price/item_quantity)

		tools.updatePrices(self.priceList)

	def addCupboard(self):

		cupboard = tools.getCupboard()

		while True:
			item_name = input("Name: ")

			if item_name == "###":
				print("Exiting.")
				break

			if item_name in cupboard.keys():
				cupboard[item_name].quantity += self.priceList[item_name].quantity
			elif item_name in self.priceList.keys():
				cupboard[item_name] = self.priceList[item_name]
			else:
				print("Item does not exist. Please try again.")
				continue

			print("Successfully added to cupboard.")

		tools.updateCupboard(self.priceList)

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

				if ingredient_name == "###":
					if ingredients:
						meals_to_add.append(Meal(meal_name, ingredients))
						print("Meal has been added.")
						break
					else:
						print("No ingredients. Please put ingredients")
						continue

				try:
					ingredient_price = self.priceList[ingredient_name].price
				except KeyError:
					print("No such item exists. Please try again.")
					continue

				ingredient_quantity = float(input("Ingredient quantity: "))

				ingredients.append(FoodItem(ingredient_name, ingredient_quantity, ingredient_price))
				print("Ingredient has been added.")

		meals = tools.getMeals() + meals_to_add
		tools.updateMeals(meals)


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

