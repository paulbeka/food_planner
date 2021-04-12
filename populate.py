from food_planner.meal import Meal
from food_planner.foodItem import FoodItem
from main import updateMeal, updateCupboard


def main():

	foodList = []
	mealList = []
	priceList = []

	foodList.append(FoodItem("chicken",200,2))
	foodList.append(FoodItem("steak",250,5))
	foodList.append(FoodItem("pork",300,2))
	foodList.append(FoodItem("onions",100,1.6))
	foodList.append(FoodItem("asparagus",50,2))
	foodList.append(FoodItem("nutella",1000,4.5))
	foodList.append(FoodItem("pizza",250,2.5))

	mealList.append(Meal("chicken_onions", [foodList[0], foodList[3]]))
	mealList.append(Meal("pork_asparagus", [foodList[2], foodList[4]]))
	mealList.append(Meal("pizza_chicken", [foodList[0], foodList[6]]))
	mealList.append(Meal("nutella_steak", [foodList[5], foodList[1]]))
	mealList.append(Meal("chicken_steak", [foodList[0], foodList[1]]))


	updateCupboard(foodList)
	updateMeal(mealList)


if __name__ == "__main__":
	main()
