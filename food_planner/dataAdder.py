import os, csv
from food_planner.foodItem import FoodItem
from food_planner.settings import PRICE_LOC


class dataAdder:

	def __init__(self):
		with open(PRICE_LOC, "r") as f:
			self.priceList = []

		self.exit = False


	def addPrices(self):
		
		# Loop until input is "###"
		quit = False
		while not quit:
			item_name = input("Name: ")

			if item_name == "###":
				print("Exiting.")
				quit = True

			item_price = float(input("Price: "))
			item_quantity = float(input("Quantity: "))

			self.priceList.append(FoodItem(item_name, item_price, item_quantity))

	def addMeals(self):

