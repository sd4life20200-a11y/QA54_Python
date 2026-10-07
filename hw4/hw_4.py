import csv
import json

def save_books(books):
    with open("books.txt", "w") as file:
        for book in books:
            file.write(book + "\n")


books = [
    "Harry Potter",
    "The Hobbit",
    "1984",
    "The Little Prince"
]

save_books(books)


####################################################


def read_products(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(f"Product: {row['product']} ({row['price']})")


read_products("products.csv")


####################################################


def save_user(username, email, country):
    user = {
        "username": username,
        "email": email,
        "country": country
    }
    with open("user.json", "w") as file:
        json.dump(user, file,indent=4)

save_user("anna21", "anna@example.com", "Israel")