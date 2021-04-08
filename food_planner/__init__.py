import os, pickle

meals = os.path.join(os.getcwd(), "data", "meals.csv")
items = os.path.join(os.getcwd(), "data", "cupboard.csv")

if not os.path.exists(meals):
	with open(meals, "w") as f:
		pass

if not os.path.exists(items):
	with open(items, "w") as f:
		pass