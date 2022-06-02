ingredients = {"water": 400, "milk": 540, "coffee": 120, "cups": 9, "money": 550}
espresso = {"water": 250, "coffee": 16, "cups": 1, "money": -4}
latte = {"water": 350, "milk": 75, "coffee": 20, "cups": 1, "money": -7}
cappuccino = {"water": 200, "milk": 100, "coffee": 12, "cups": 1, "money": -6}
options = {"1": "espresso", "2": "latte", "3": "cappuccino"}


def main():
    return eval(input("Write action (buy, fill, take, remaining, exit):\n") + "()")


def remaining():
    print(f"""\nThe coffee machine has:
{ingredients["water"]} ml of water
{ingredients["milk"]} ml of milk
{ingredients["coffee"]} g of coffee beans
{ingredients["cups"]} disposable cups
${abs(ingredients["money"])} of money\n""")
    return main()


def buy():
    choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if choice == "back":
        return main()
    for key, value in eval(options[choice]).items():
        if value > ingredients[key]:
            print(f"Sorry, not enough {key}!\n")
            return main()
    print("I have enough resources, making you a coffee!\n")
    for key, value in eval(options[choice]).items():
        ingredients[key] -= value
    return main()


def fill():
    msg = ("\nWrite how many ml of water you want to add:\n",
           "Write how many ml of milk you want to add:\n",
           "Write how many grams of coffee beans you want to add\n",
           "Write how many disposable cups of coffee you want to add:\n")
    for count, key in enumerate(ingredients):
        if count <= 3:
            ingredients[key] += int(input(msg[count]))
    return main()


def take():
    print(f"\nI gave you ${ingredients['money']}\n")
    ingredients['money'] = 0
    return main()


main()
