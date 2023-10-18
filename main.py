import coffee


def main():
    while True:
        choice = which_coffee()
        calculate_ingredients(choice)
        insert_coin(choice)
        if choice == 'off':
            break

def which_coffee():
    while True:
        try:
            choice = str(input("“What would you like? (espresso/latte/cappuccino): "))
            if choice == "espresso" or choice == "latte" or choice == "cappuccino":
                return choice
            elif choice == "off":
                break
            elif choice == "report":
                print_report()
                continue
            else:
                continue
        except ValueError:
            print("Please enter espresso/latte/cappuccino only")
            pass


def print_report():
    print("Water:", coffee.INGREDIENTS["water"], "ml")
    print("Milk:", coffee.INGREDIENTS["milk"], "ml")
    print("Coffee:", coffee.INGREDIENTS["coffee"], "g")
    print("Money:", coffee.MONEY["money"], "$")


def calculate_ingredients(choice):
    if choice == "latte" or choice == "cappuccino":
        coffee.INGREDIENTS["water"] = int(coffee.INGREDIENTS["water"]) - int(
            coffee.MENU[choice]["ingredients"]["water"]
        )
        coffee.INGREDIENTS["milk"] = int(coffee.INGREDIENTS["milk"]) - int(
            coffee.MENU[choice]["ingredients"]["milk"]
        )
        coffee.INGREDIENTS["coffee"] = int(coffee.INGREDIENTS["coffee"]) - int(
            coffee.MENU[choice]["ingredients"]["coffee"]
        )
    elif choice == "espresso":
        coffee.INGREDIENTS["coffee"] = int(coffee.INGREDIENTS["coffee"]) - int(
            coffee.MENU[choice]["ingredients"]["coffee"]
        )
        coffee.INGREDIENTS["water"] = int(coffee.INGREDIENTS["water"]) - int(
            coffee.MENU[choice]["ingredients"]["water"]
        )

    if coffee.INGREDIENTS["water"] < 0:
        print("Missing Water:", -abs(coffee.INGREDIENTS["water"]), "ml")
        exit()
    elif coffee.INGREDIENTS["milk"] < 0:
        print("Missing Milk:", -abs(coffee.INGREDIENTS["water"]), "ml")
        exit()
    elif coffee.INGREDIENTS["coffee"] < 0:
        print("Missing Coffee:", -abs(coffee.INGREDIENTS["water"]), "ml")
        exit()


def insert_coin(choice):
    money_dict = {}
    money = 0
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money_dict = {
        "quarters":quarters,
        "dimes":dimes,
        "nickles":nickles,
        "pennies":pennies
    }
    money = money_dict["quarters"]*0.25 + money_dict["dimes"] * 0.10 + money_dict["nickles"] * 0.05 + money_dict["pennies"] * 0.01
    print("Inserted :",money)
    print("Coffee cost:",coffee.MENU[choice]['cost'])
    if money < coffee.MENU[choice]['cost']:
        print("You don`t have enough money to buy coffee")
        exit()
    else:
        print("Your change is:", money-int(coffee.MENU[choice]['cost']),"$")




if __name__ == "__main__":
    main()
