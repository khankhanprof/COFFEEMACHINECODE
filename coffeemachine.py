from main import resources

newwater = resources["water"]
newmilk = resources["milk"]
newcoffee = resources["coffee"]


def resourceupdate(a, b, c):
    global newwater, newmilk, newcoffee
    if a == 0 and b == 0 and c == 0:
        print(f"water: {newwater},milk:{ newmilk},coffee: {newcoffee}")
    elif a <= newwater and b <= newmilk and c <= newcoffee:
        newwater -= a
        newmilk -= b
        newcoffee -= c
        return True
    else:
        print("insufficient resources")
        return newwater, newmilk, newcoffee


def coinsufficiency(value):
    coinpenny = int(input("enter the number of pennies:"))
    coinnickle = int(input("enter the number of nickle:"))
    coindime = int(input("enter the number of dime:"))
    coinquarter = int(input("enter the number of quarters:"))
    total = coinpenny * 0.01 + coinnickle * 0.05 + coindime * 0.10 + coinquarter * 0.25
    if total == value:
        print("your espresso is ready ,thanks for shopping !!")
    elif total > value:
        remain=total-value
        print(f"here is your change:{round(remain,2)}")
        print("your espresso is ready ,thanks for shopping !!")
    elif total < value:
        print("insufficient money")





p = True
while p:
    inputdata = input(
        'what would you like to have (espresso/latte/cappuccino)(or)"report"-availability of resources(or) OFF-to switch off: ').lower()
    if inputdata=="off":
        print("machine shutting down !!!")
        p=False
    elif inputdata == "report":
        resourceupdate(0, 0, 0)
    elif inputdata == "espresso":
        output = resourceupdate(50, 0, 18)
        if output:
            coinsufficiency(1.50)


    elif inputdata == "latte":
        output = resourceupdate(200, 150, 24)
        if output:
            coinsufficiency(2.50)


    elif inputdata == "cappuccino":
        output = resourceupdate(250, 100, 24)
        if output:
            coinsufficiency(2.50)



