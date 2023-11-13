"""
Markdown Table Generator for Chemical Elements

This script takes data about chemical elements from a CSV file, allows the user to input
a group or period, selects the elements matching the input, and generates a Markdown table.
The Markdown table is saved to an output file.

Usage:
1. Run the script.
2. Enter 'group' or 'period' when prompted.
3. Enter the group name or period number accordingly.
4. The script will create a Markdown file containing information about the selected group or period.

Author: Pavel
"""

import pandas as pd

# Function to create a Markdown table from a DataFrame of chemical elements
def create_markdown_table(elements):
    """
    Create a Markdown table from a DataFrame containing information about chemical elements.

    Parameters:
    - elements (pd.DataFrame): DataFrame containing information about chemical elements.

    Returns:
    str: Markdown content representing the table.
    """
    markdown_content = "## Overview of Elements\n\n"
    markdown_content += "| Symbol | Element | Atomic Number | Atomic Mass |  Group | Period |\n"
    markdown_content += "|--------|--------|---------------|-------------|-------|--------|\n"

    required_columns = ['Symbol', 'Element', 'AtomicNumber', 'AtomicMass', 'Type', 'Period']

    # Check if required columns are present in the DataFrame
    missing_columns = set(required_columns) - set(elements.columns)
    if missing_columns:
        raise ValueError(f"Missing columns in the DataFrame: {missing_columns}")

    # Iterate over rows in the DataFrame and populate the Markdown table
    for index, row in elements.iterrows():
        symbol = row['Symbol']
        name = row['Element']
        atomic_number = row['AtomicNumber']
        atomic_mass = row['AtomicMass']
        element_type = row['Type']
        period = row['Period']

        markdown_content += f"| {symbol} | {name} | {atomic_number} | {atomic_mass} | {element_type}  | {period} |\n"

    return markdown_content

# Function to save Markdown content to a file
def save_to_markdown(markdown_content, output_file):
    """
    Save the Markdown content to a file.

    Parameters:
    - markdown_content (str): Markdown content to be saved.
    - output_file (str): The path to the Markdown file where the content will be saved.
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

# Main function
def main():
    """
    Main function to run the Markdown Table Generator for Chemical Elements.
    """
    # Load CSV data using pandas
    elements = pd.read_csv('elements.csv')

    # Get user input for category ('group' or 'period')
    category = input("Enter 'group' or 'period' : ").lower()

    if category == 'group':
        # For group input, get the group name from the user
        group = input("Enter the group name: ")
        elements_in_group_or_period = elements[(elements['Type'].str.lower() == group.lower())]
        group_b = group.replace(" ", "_")

        if not elements_in_group_or_period.empty:
            # Generate and save Markdown table for the specified group
            markdown_table = create_markdown_table(elements_in_group_or_period)
            save_to_markdown(markdown_table, f'{group_b}.md')
            print(f"Markdown file '{group_b}.md' created successfully.")
        else:
            print(f"No elements found in Group or Period.")
    elif category == 'period':
        # For period input, get the period number from the user
        period_number = input("Enter the period number (1-7): ")
        elements_in_group_or_period = elements[(elements['Period'] == int(period_number))]

        if not elements_in_group_or_period.empty:
            # Generate and save Markdown table for the specified period
            markdown_table = create_markdown_table(elements_in_group_or_period)
            save_to_markdown(markdown_table, f'Period{period_number}.md')
            print(f"Markdown file 'Period{period_number}.md' created successfully.")
        else:
            print(f"No elements found in Group or Period.")
    else:
        print("Invalid input. Please enter 'group' or 'period'.")
        return