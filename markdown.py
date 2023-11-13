import pandas as pd

def create_markdown_table(elements):
    markdown_content = "## Overview of Elements\n\n"
    markdown_content += "| Symbol | Element | Atomic Number | Atomic Mass |  Group | Period |\n"
    markdown_content += "|--------|------|---------------|-------------|-------|--------|\n"

    required_columns = ['Symbol', 'Element', 'AtomicNumber', 'AtomicMass', 'Type', 'Period']

    missing_columns = set(required_columns) - set(elements.columns)
    if missing_columns:
        raise ValueError(f"Missing columns in the DataFrame: {missing_columns}")

    for index, row in elements.iterrows():
        symbol = row['Symbol']
        name = row['Element']
        atomic_number = row['AtomicNumber']
        atomic_mass = row['AtomicMass']
        element_type = row['Type']
        period = row['Period']

        markdown_content += f"| {symbol} | {name} | {atomic_number} | {atomic_mass} | {element_type}  | {period} |\n"

    return markdown_content

def save_to_markdown(markdown_content, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

def main():
    # Load CSV data using pandas
    elements = pd.read_csv('elements.csv')

    category = input("Enter 'group' or 'period' to calculate average atomic mass: ").lower()

    if category == 'group':
        group = input("Enter the group name: ")
        elements_in_group_or_period = elements[(elements['Type'].str.lower() == group.lower())]
        group_b = group.replace(" ", "_")

        if not elements_in_group_or_period.empty:
            markdown_table = create_markdown_table(elements_in_group_or_period)
            save_to_markdown(markdown_table, f'{group_b}.md')
            print(f"Markdown file '{group_b}.md' created successfully.")
        else:
            print(f"No elements found in Group or Period.")
    elif category == 'period':
        period_number = input("Enter the period number (1-7): ")
        elements_in_group_or_period = elements[(elements['Period'] == int(period_number))]

        if not elements_in_group_or_period.empty:
            markdown_table = create_markdown_table(elements_in_group_or_period)
            save_to_markdown(markdown_table, f'Period{period_number}.md')
            print(f"Markdown file 'Period{period_number}.md' created successfully.")
        else:
            print(f"No elements found in Group or Period.")
    else:
        print("Invalid input. Please enter 'group' or 'period'.")
        return


