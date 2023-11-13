"""
HTML Table Generator

This script takes a CSV file containing data about chemical elements and generates an HTML table.
The HTML table is saved to an output file.

Usage:
gen_html(input_file, output_file)

Parameters:
- input_file (str): The path to the input CSV file containing data about chemical elements.
- output_file (str): The path to the output HTML file where the generated table will be saved.

Author: Luky
"""
import csv


def gen_html(input_file, output_file):
    """
    Generate an HTML table from a CSV file containing data about chemical elements.

    Parameters:
    - input_file (str): The path to the input CSV file containing data about chemical elements.
    - output_file (str): The path to the output HTML file where the generated table will be saved.
    """
    # Read data from the CSV file into a list of dictionaries
    with open(input_file, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)

    # HTML content template
    html_content = """
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
            }
            table, th, td {
                border: 1px solid black;
            }
            th, td {
                padding: 8px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1>Periodic Table</h1>
        <table>
            <tr>
                <th>Atomic Number</th>
                <th>Element</th>
                <!-- Add other table headers based on your CSV columns -->
            </tr>
    """

    # Add rows to the HTML content based on the data from the CSV file
    for row in data:
        html_content += "<tr>"
        for value in row.values():
            html_content += f"<td>{value}</td>"
        html_content += "</tr>"

    # Closing HTML tags
    html_content += """
        </table>
    </body>
    </html>
    """

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)