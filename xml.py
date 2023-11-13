import pandas as pd

def load_elements_from_csv(csv_file):
    return pd.read_csv(csv_file)

def export_to_xml(selected_elements, xml_file):
    selected_elements.to_xml(xml_file, index=False)

def main():
    # Load CSV data using pandas
    elements = load_elements_from_csv('elements.csv')

    phrase = input("Enter name of the element: ")

    selected_elements = elements[elements['Element'].str.lower() == phrase.lower()]

    if not selected_elements.empty:
        export_to_xml(selected_elements, 'selected_elements.xml')
        print("XML file 'selected_elements.xml' created successfully.")
    else:
        print("No elements found for export.")

