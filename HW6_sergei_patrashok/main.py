def get_product(products, index):
    try:
        return products[index]
    except IndexError:
        return "Product index is out of range"


products = ["coffee", "tea", "milk"]

print(get_product(products, 0))
print(get_product(products, 7))








def get_settings_value(settings, key):
    try:
        return settings[key]
    except KeyError:
        return "Setting was not found"


settings = {
    "language": "English",
    "theme": "dark"
}

print(get_settings_value(settings, "theme"))
print(get_settings_value(settings, "font"))