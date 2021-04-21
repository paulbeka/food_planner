import random, csv, os, sys
from food_planner.meal import Meal
from food_planner.foodItem import FoodItem
from food_planner.tools import getItems, getMeals, updateCupboard
from food_planner.dataAdder import DataAdder
from food_planner.calculator import Calculator


def runCalculator(mode, budget, time):

	calculator = Calculator(budget, time)

	meal_plan = calculator.run(mode)
	if meal_plan == None:
		print("No meal plan can be calculated.")
		return
	
	for item in meal_plan:
		print(item.name)


def main():

	if len(sys.argv) > 1:
		if "-a" in sys.argv:
			DataAdder().run()

		elif sys.argv[1] == "-c" and len(sys.argv) == 4:
			runCalculator(False, int(sys.argv[2]), int(sys.argv[3]))

		elif sys.argv[1] == "-m" and len(sys.argv) == 4:
			runCalculator(True, int(sys.argv[2]), int(sys.argv[3]))

		else:
			print("Error: format needs to be in the form:")
			print("python3 main.py <command> <budget> <time>")
	

if __name__ == "__main__":
	main()