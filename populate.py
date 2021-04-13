from food_planner.meal import Meal
from food_planner.foodItem import FoodItem
from food_planner.tools import updateMeal, updateCupboard


def main():

	foodList = []
	mealList = []
	priceList = []

	foodDict = {}

	foodList.append(FoodItem("chicken",200,2/200))
	foodList.append(FoodItem("steak",250,5/250))
	foodList.append(FoodItem("pork",300,2/300))
	foodList.append(FoodItem("onions",100,1.6/100))
	foodList.append(FoodItem("asparagus",50,2/50))
	foodList.append(FoodItem("nutella",1000,4.5/1000))
	foodList.append(FoodItem("pizza",250,2.5/250))
	foodList.append(FoodItem("tortilla", 8, 8/2))

	for item in foodList:
		foodDict[item.name] = item

	mealList.append(Meal("chicken_onions", [FoodItem("chicken", 500, 2/200), foodList[3]]))
	mealList.append(Meal("pork_asparagus", [foodList[2], foodList[4]]))
	mealList.append(Meal("pizza_chicken", [FoodItem("chicken", 500, 2/200), foodList[6]]))
	mealList.append(Meal("nutella_steak", [FoodItem("nutella", 50, 4.5/1000), FoodItem("steak", 50, 5/250)]))
	mealList.append(Meal("chicken_steak", [FoodItem("chicken", 500, 2/200), FoodItem("steak", 50, 5/250)]))
	mealList.append(Meal("tortilla_tortilla", [FoodItem("tortilla",2,2/8)]))


	updateCupboard(foodDict)
	updateMeal(mealList)


if __name__ == "__main__":
	main()
