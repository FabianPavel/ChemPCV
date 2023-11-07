import csv


def gen_html(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)

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
                <!-- (rest of your table headers) -->
            </tr>
    """

    for row in data:
        html_content += "<tr>"
        for value in row.values():
            html_content += f"<td>{value}</td>"
        html_content += "</tr>"

    html_content += """
        </table>
    </body>
    </html>
    """

    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)
