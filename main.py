import sys
from food_planner.dataAdder import DataAdder
from food_planner.calculator import Calculator
from food_planner.contact import PhoneMessenger


def run(mode, budget, time):

	calculator = Calculator(budget, time)

	meal_plan = calculator.run(mode)

	if meal_plan == None:
		return

	# Make a string of all menu items
	data_string = ""
	for item in meal_plan:
		data_string += item.name + ","

	phoneContact = PhoneMessenger()
	phoneContact.sendMessage(data_string)

	if not mode:
		pass
	else:
		# send shopping list to user
		pass

def main():

	# Handle command line arguments
	if len(sys.argv) > 1:
		if "-a" in sys.argv:
			DataAdder().run()

		elif sys.argv[1] == "-c" and len(sys.argv) == 4:
			run(False, int(sys.argv[2]), int(sys.argv[3]))

		elif sys.argv[1] == "-m" and len(sys.argv) == 4:
			run(True, int(sys.argv[2]), int(sys.argv[3]))

		else:
			print("Error: format needs to be in the form:")
			print("python3 main.py <command> <budget> <time>")
	

if __name__ == "__main__":
	main()