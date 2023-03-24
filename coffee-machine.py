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
is_on = True

while True:
    choice = input("What would you like? (espresso/latte/cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print("Water: 100ml")
        print("Milk: 50ml")
        print("Coffe: 76g")
        print("MOney: $2.5")
