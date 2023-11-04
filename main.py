import csv
import json

from html_table import gen_html


def load_elements_from_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        groups = json.load(file)
    return groups

def load_elements_from_csv(csv_file):
    elements = []
    with open(csv_file, 'r', encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            elements.append(row)
    return elements


def search(elements, phrase):
    found = []
    for element in elements:
        if phrase.lower() == element[1].lower() or phrase.lower() == element[2].lower():
            found.append(element)
    return found


def display(elements):
    for element in elements:
        print(element)


elements = load_elements_from_csv('elements.csv')
groups = load_elements_from_json('groups.json')

while True:
    print("1. Display all elements")
    print("2. Display all groups")
    print("3. create html table")
    print("10. Search for element by name or symbol")
    print("0. exit")
    choice = input("Enter your choice: ")

    if choice == "0":
        print("Closing the application. Goodbye")
        break
    elif choice == "1":
        print("displaying all elements: ")
        display(elements)
    elif choice == "2":
        print("displaying all groups: ")
        display(groups)
    elif choice == "3":
        print("created html table ")
        gen_html("elements.csv", 'periodic_table.html')
    elif choice == "10":
        phrase = input("Enter name or symbol of element to search for: ")
        found = search(elements, phrase)
        if found:
            display(found)
        else:
            print("Element not found. Please try again.")
    else:
        print("Invalid choice. Please try again.")