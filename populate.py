from food_planner.settings import ITEM_LOC, PRICE_LOC, MEAL_LOC


PRICES = """chicken2breast,300.0,0.006
eggs,12.0,0.170833333
ham,10.0,0.1
tortilla_wraps,8.0,0.11875
edam,10.0,0.175
2avocado,2.0,1.25
4_pork_loins,4.0,0.75
petit_pois,1000.0,0.0013
baby_potatoes,1000.0,0.001
asparagus_tips,125.0,0.0144
2_salmon,2.0,1.625
spagetti,1000.0,0.001
bolognese,1000.0,0.00064
smoked_bacon_lardons,2.0,1.0
sausages,12.0,0.20833333333333334
carrots,1000.0,0.0004
couscous,500.0,0.0014
red_onions,3.0,0.2833333333333333
peppers,3.0,0.45
minced_beef,500.0,0.005
corn_can,200.0,0.0034999999999999996
mixed_frozen_veggies,1000.0,0.00079
sliced_bread,20.0,0.05500000000000001
hash_browns,15.0,0.08
gnocci,500.0,0.0015
pepperoni_pizza,1.0,3.5
meal_deal,1.0,3.0
"""

MEALS = """tortillas,tortilla_wraps:2.0:0.11875,ham:5.0:0.1,edam:2.0:0.175,2avocado:0.5:1.25
pork_hash_petitpois,4_pork_loins:2.0:0.75,petit_pois:200.0:0.0013,hash_browns:5.0:0.08
spaghetti bolognese,spagetti:200.0:0.001,bolognese:250.0:0.00064,minced_beef:500.0:0.005
beef and corn,corn_can:200.0:0.0034999999999999996,minced_beef:250.0:0.005,couscous:150.0:0.0014
eggs and potatoes,eggs:3.0:0.170833333,baby_potatoes:330.0:0.001
eggs_poatoes_carrots,baby_potatoes:330.0:0.001,eggs:3.0:0.170833333,carrots:200.0:0.0004
carbonara,spagetti:200.0:0.001,smoked_bacon_lardons:1.0:1.0,red_onions:0.5:0.2833333333333333,eggs:1.0:0.170833333
sasage_veggies_potatoes,sausages:6.0:0.20833333333333334,baby_potatoes:330.0:0.001,mixed_frozen_veggies:250.0:0.00079
"""
CUPBOARD = """"""

def main():

	with open(ITEM_LOC, "w") as f:
		f.write(PRICES)

	with open(PRICE_LOC, "w") as f:
		f.write(PRICES)

	with open(MEAL_LOC, "w") as f:
		f.write(MEALS)


if __name__ == "__main__":
	main()
