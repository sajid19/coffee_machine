MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}


def resources_sufficient(order_ingredients):

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry not sufficient{item}. ")
            return False
    return True


def process_coins():

    """Return the total calculated from coin inserted"""
    print("please insert coins")
    total = int(input("how many quarters? :"))* 0.25
    total += int(input("how many dimes? :")) * 0.1
    total += int(input("how many nickles? :")) * 0.05
    total += int(input("how many pennies? :")) * 0.01

    return total


def transaction_successfull(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is your {change}$ change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry not enough money")
        return False


def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")


is_on = True
while is_on:

  choice = input("what would you like to have? espresso/latte/capuccino: ")

  if is_on == "off":

   is_on = False

  elif choice == "report":
    print(f"water:{resources['water']}ml")
    print(f"milk:{resources['milk']}ml")
    print(f"coffee:{resources['coffee']}g")
    print(f"money:$ {profit}")

  else:
     drink = MENU[choice]
     if resources_sufficient(drink["ingredients"]):
         payment = process_coins()
         if transaction_successfull(payment, drink["cost"]):
            make_coffee(choice, drink["ingredients"])






















