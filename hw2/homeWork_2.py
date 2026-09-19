def clean_cart(cart):
    while "sold out" in cart:
        cart.remove("sold out")
    return cart

print(clean_cart(["milk", "sold out", "bread", "sold out", "coffee"]))



def temperature_report(temperatures):
    result = []

    for temperature in temperatures:
        if temperature > 25:
            result.append(temperature)

    return result

print(temperature_report([21, 28, 19, 31, 25, 27]))



def fix_balances(balances):
    for i in range(len(balances)):
        if balances[i] < 0:
            balances[i] = 0
    return balances

print(fix_balances([120, -30, 50, -5, 0, 200]))



def unique_items(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result

print(unique_items(["red", "blue", "red", "green", "blue"]))