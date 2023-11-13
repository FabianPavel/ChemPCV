"""
Chemistry Toolkit

This script provides a simple command-line interface for various chemistry-related operations,
including displaying elements and groups, generating HTML tables, calculating average atomic mass,
creating markdown files, generating XML files, and searching for elements by name or symbol.

Dependencies:
- pandas
- html_table
- calc (assumed to be a separate module with a 'main' function)
- markdown (assumed to be a separate module with a 'main' function)
- xml (assumed to be a separate module with a 'main' function)

Author: Luky & Pavel
"""

# Importing necessary modules
import pandas as pd
from html_table import gen_html
import calc
import markdown
import xml


def search(elements, phrase):
    """
    Search for an element by name or symbol in the given DataFrame.

    Parameters:
    - elements (pd.DataFrame): DataFrame containing information about chemical elements.
    - phrase (str): Name or symbol of the element to search for.

    Returns:
    pd.DataFrame: DataFrame containing the found element(s) or an empty DataFrame if not found.
    """
    condition = (elements['Element'] == phrase) | (elements['Symbol'] == phrase)
    return elements[condition]


def main():
    """
    Main function to run the chemistry toolkit.

    Displays a menu with options for different chemistry-related operations and performs the selected operation.
    """
    # Setting pandas display options
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    # Reading data from CSV and JSON files
    elements = pd.read_csv('elements.csv')
    groups = pd.read_json('groups.json')

    while True:
        # Displaying menu options
        print("1. Display all elements")
        print("2. Display all groups")
        print("3. Create html table")
        print("4. Calculate average atomic mass")
        print("5. Create markdown file with specific period or group")
        print("6. Create xml file with wanted element")
        print("7. Search for element by name or symbol")
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
        elif choice == "6":
            xml.main()
        elif choice == "7":
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