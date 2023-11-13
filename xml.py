"""
XML Exporter for Selected Elements

This script loads data about chemical elements from a CSV file, allows the user to input
the name of an element, selects the elements matching the input name, and exports the selected
elements to an XML file.

Usage:
1. Run the script.
2. Enter the name of the element when prompted.
3. The script will create an XML file containing information about the selected element.

Author: Pavel
"""
import pandas as pd


def load_elements_from_csv(csv_file):
    """
    Load data about chemical elements from a CSV file using pandas.

    Parameters:
    - csv_file (str): The path to the CSV file containing data about chemical elements.

    Returns:
    pd.DataFrame: DataFrame containing information about chemical elements.
    """
    return pd.read_csv(csv_file)


def export_to_xml(selected_elements, xml_file):
    """
    Export selected elements to an XML file.

    Parameters:
    - selected_elements (pd.DataFrame): DataFrame containing the selected elements.
    - xml_file (str): The path to the XML file where the selected elements will be exported.
    """
    selected_elements.to_xml(xml_file, index=False)


def main():
    """
    Main function to run the XML Exporter for Selected Elements.
    """
    # Load CSV data using pandas
    elements = load_elements_from_csv('elements.csv')

    # Get user input for the name of the element
    phrase = input("Enter the name of the element: ")

    # Select elements matching the input name
    selected_elements = elements[elements['Element'].str.lower() == phrase.lower()]

    # Check if any elements were selected
    if not selected_elements.empty:
        # Export selected elements to XML
        export_to_xml(selected_elements, 'selected_elements.xml')
        print("XML file 'selected_elements.xml' created successfully.")
    else:
        print("No elements found for export.")