import random
import os
user_input = input

def make_sale(user_input):
	
	print("Type the item you wish to purchase like so: 'Potion', without the quotes.")
	input("\nPress enter to continue...")
	print("Welcome to my shop.\n")
	shop = ["Potion - 5GP", "Shield - 10GP", "Sword - 15GP"]
	inventory = []
	attempts = len(shop)
	gold = random.randint(8, 35)
	costs = [5, 10, 15]
			
	while attempts > 0:
		
		attempts = len(shop)
		os.system('cls')
		
		if attempts == 0 or gold < min(costs):
			print("The shop has nothing left to offer.")
			print("\nInventory: " + str(inventory))
			print("\nGold:" + str(gold))
			exit()
			
		print("Shop: " + str(shop))
		print("Inventory: " + str(inventory))
		print("\nGold:" + str(gold))
		user_input = input("\nWhich item would you like to buy?\n")
		
		if user_input.title() == "Potion":
			print("\nYou buy the potion.")
			print("\n    |~|")
			print("    | |")
			print("  .'   `.")
			print("  `.___.'")
			gold = gold -5
			shop.remove("Potion - 5GP")
			costs.remove(5)
			inventory.append("Potion")
			print("\nYou have " + str(gold) + " gold remaining.")
			input("\nPress enter to continue...")
			os.system('cls')
			
		elif user_input.title() == "Shield":
			if gold >= 10:
				print("\nYou buy the shield.")
				gold += -10
				print("\n    |`-._/\_.-`|")
				print("    |    ||    | ")
				print("    |___o()o___|")
				print("    |__((<>))__|")
				print("    \   o\/o   /")
				print("     \   ||   /")
				print("      \  ||  /")
				print("       '.||.'")
				print("         ``")
				shop.remove("Shield - 10GP")
				costs.remove(10)
				inventory.append("Shield")
				print("\nYou have " + str(gold) + " gold remaining.")
				input("\nPress enter to continue...")
				os.system('cls')
			elif gold < 10:
				print("\nYou don't have enough money!\n")
				input("\nPress enter to continue...")
				os.system('cls')
				
		elif user_input.title() == "Sword":
			if gold >= 15:
				print("\nYou buy the sword.")
				gold += -15
				print("\n         />")
				print("        //")
				print("[////<*>|||<===============================")
				print("        \\\\")
				print("         \>")
				shop.remove("Sword - 15GP")
				costs.remove(15)
				inventory.append("Sword")
				print("\nYou have " + str(gold) + " gold remaining.")
				input("\nPress enter to continue...")
				os.system('cls')
			elif gold < 15:
				print("\nYou don't have enough money!\n")
				input("\nPress enter to continue...")
				os.system('cls')
				
make_sale(user_input)
