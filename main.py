import random, csv, os, sys
from food_planner.meal import Meal
from food_planner.foodItem import FoodItem
from food_planner.tools import getItems, getMeals, updateCupboard
from food_planner.dataAdder import DataAdder
from food_planner.calculator import Calculator


def runCalculator():

	budget = 50
	time = 7

	calculator = Calculator(budget, time)

	meal_plan = calculator.run(True)
	if meal_plan == None:
		print("No meal plan can be calculated.")
		return
	
	for item in meal_plan:
		print(item.name)


def main():

	if len(sys.argv) > 1:
		if "-a" in sys.argv:
			DataAdder().run()

		if "-c" in sys.argv:
			runCalculator()

		if "-m" in sys.argv:
			runCalculator()
	

if __name__ == "__main__":
	main()