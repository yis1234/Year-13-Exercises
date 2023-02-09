Bread_Prices = {
    "Wholemeal": 1.00,
    "White": 0.80,
    "Cheesy White": 1.20,
    "Gluten Free": 1.40}

Meat_Prices = {
    "Chicken": 2.69,
    "Beef": 3.00,
    "Salami": 4.00,
    "Vegan Slice": 3.30}

Garnish_Prices = {
    "Onion": 1.69,
    "Tomato": 1.00,
    "Lettuce": 2.00,
    "Cheese": 2.50}


def sandwich_maker():
    print("Hello and welcome to the sandwich maker")
    print("Please select your bread: ")
    for bread in Bread_Prices:
        print(bread)
    bread_choice = input("Please enter your bread choice: ").capitalize()
    print("Please select your meat:")
    for meat in Meat_Prices:
        print(meat)
    meat_choice = input("Please enter your meat choice: ").capitalize()
    print("Please select your garnish:")
    for garnish in Garnish_Prices:
        print(garnish)
    garnish_choice = input("Please enter your garnish choice: ").capitalize()
    print(f"Your current order contains: Bread: {bread_choice} "
          f"Meat: {meat_choice} Garnish: {garnish_choice}")
    print(f"Your sandwich will cost: "
          f"${str(Bread_Prices[bread_choice] + Meat_Prices[meat_choice] + Garnish_Prices[garnish_choice])}")
    confirm = input("Would you like to confirm your order? (Y/N) ").upper()
    if confirm == "Y":
        print("Thank you for your order!")
    else:
        print("Please make your changes.")
        sandwich_maker()


sandwich_maker()
