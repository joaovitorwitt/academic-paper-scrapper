import json
import time




def get_user_input(prompt):
    while True:
        try:
            string = input(prompt).strip()
            return string
        except:
            print("Something went wrong")


# function that search for a specify function on a json file
def search_books():
    filepath = "./books.json"

    searched_book = get_user_input("Enter a book name: ").strip()

    with open(filepath, "r") as file:
        data = json.load(file)

    for book in data:
        if searched_book.strip().lower() in book['title'].strip().lower():
            result = f"FOUND: {book['title']}"
            print("Searching for book....")
            time.sleep(3)
            return result
        else:
            result = "NOT FOUND"

    return result
