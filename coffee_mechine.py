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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"sorry there is not sufficient{item}")
            return False
        return True

def process_coins():
    total= int(input("enter the number of pennies"))*.01
    total += int(input("enter the number of nickels")) * .05
    total += int(input("enter the number of dime")) * .1
    total += int(input("enter the number of quarters")) * .25
    return total

def is_transaction_sucessful(money_recived,drink_cost):
    if money_recived >= drink_cost:
        change= round(money_recived-drink_cost,2)
        print(f"here is your {change}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("sorry the money is not sufficient hare is your money back")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"here is your  {drink_name} enjoy")

is_on= True
while is_on:
    choice = input( "What would you like? (espresso/latte/cappuccino):")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water{resources['water']}ml")
        print(f"milk{resources['milk']}ml")
        print(f"coffee{resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_sucessful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])

