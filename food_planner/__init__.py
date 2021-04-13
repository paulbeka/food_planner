import os, pickle
from food_planner.settings import ITEM_LOC, PRICE_LOC, MEAL_LOC

if not os.path.exists(MEAL_LOC):
	with open(MEAL_LOC, "w") as f:
		pass

if not os.path.exists(ITEM_LOC):
	with open(ITEM_LOC, "w") as f:
		pass

if not os.path.exists(PRICE_LOC):
	with open(PRICE_LOC, "w") as f:
		pass