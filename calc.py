"""
Average Atomic Mass Calculator

This script calculates the average relative atomic mass for a given group or period of chemical elements.

Usage:
1. Run the script.
2. Enter 'group' or 'period' when prompted.
3. Enter the group number (1-18) or period number (1-7) accordingly.
4. The script will calculate and display the average relative atomic mass for the specified group or period.


Author: Luky
"""
import csv


def calculate_average_atomic_mass(data, key, value):
    """
    Calculate the average relative atomic mass for elements in a given group or period.

    Parameters:
    - data (list): List of dictionaries containing data about chemical elements.
    - key (str): The key (column name) to filter elements based on (e.g., 'Group' or 'Period').
    - value (str): The value to filter elements based on (e.g., group number or period number).

    Returns:
    float: The average relative atomic mass for the specified group or period, or None if no elements are found.
    """
    count = 0
    total_atomic_mass = 0

    for element in data:
        if element[key] == value:
            count += 1
            total_atomic_mass += float(element['AtomicMass'])

    if count == 0:
        return None
    else:
        return total_atomic_mass / count


def main():
    """
    Main function to run the Average Atomic Mass Calculator.
    """
    # Read the CSV file into a list of dictionaries
    with open('elements.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        elements_data = list(reader)

    # Get user input for group or period
    category = input("Enter 'group' or 'period' to calculate average atomic mass: ").lower()

    if category == 'group':
        group_number = input("Enter the group number (1-18): ")
        average_mass = calculate_average_atomic_mass(elements_data, 'Group', group_number)
    elif category == 'period':
        period_number = input("Enter the period number (1-7): ")
        average_mass = calculate_average_atomic_mass(elements_data, 'Period', period_number)
    else:
        print("Invalid input. Please enter 'group' or 'period'.")
        return

    if average_mass is not None:
        print(f"\nAverage relative atomic mass for {category} {group_number if category == 'group' else period_number}: {average_mass:.3f}\n")
    else:
        print(f"No elements found for {category} {group_number if category == 'group' else period_number}.")
