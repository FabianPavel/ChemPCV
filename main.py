import pandas as pd

from html_table import gen_html
import calc
import markdown


def search(elements, phrase):
    condition = (elements['Element'] == phrase) | (elements['Symbol'] == phrase)
    return elements[condition]


def main():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    elements = pd.read_csv('elements.csv')
    groups = pd.read_json('groups.json')

    while True:
        print("1. Display all elements")
        print("2. Display all groups")
        print("3. Create html table")
        print("4. Calculate average atomic mass")
        print("5. Create markdown file with specific period or group")
        print("10. Search for element by name or symbol")
        print("0. exit")
        choice = input("Enter your choice: ")

        if choice == "0":
            print("Closing the application. Goodbye")
            break
        elif choice == "1":
            print("displaying all elements: ")
            print(elements)
        elif choice == "2":
            print("displaying all groups: ")
            print(groups)
        elif choice == "3":
            print("created html table ")
            gen_html("elements.csv", 'periodic_table.html')
        elif choice == "4":
            calc.main()
        elif choice == "5":
            markdown.main()
        elif choice == "10":
            phrase = input("Enter name or symbol of element to search for: ")
            found = search(elements, phrase)
            if not found.empty:
                print("Element found:")
                print(found)
            else:
                print("Element not found.")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()