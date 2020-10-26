import sys

def generate_formula(month, year, row, concept):
    if int(month) < 10:
        prefix = '0'
    else:
        prefix = ''

    month_str = prefix + str(month) + "-" + str(year)

    formula = "=IF('" + month_str + " Bruto'.F" + str(row) + "=\"" + concept + "\",'" + month_str + " Bruto'.E" + str(row) + ",0)"

    return formula

def write_file(file_name, csv_lines):
    with open(file_name, mode = 'w') as file:
        for line in csv_lines:
            file.write(line)
            file.write('\n')

categories = [ 'Nómina', 'Alquiler', 'Comida', 'Ropa', 'Bizum', 'Gasolina', 'Casa', 'Otro', 'Salir', 'Teléfono', 'Viaje', 'Netflix', 'Gimnasio' ]
max_rows = 500
month = sys.argv[1]
year = sys.argv[2]

csv_lines = []

header_line = '\t'.join(categories)
csv_lines.append(header_line)

for rownum in range(1, max_rows):
    current_array = []

    for category in categories:
        formula = generate_formula(month, year, rownum, category)

        current_array.append(formula)

    csv_line = '\t'.join(current_array)

    csv_lines.append(csv_line)

write_file('output' + month + '.csv', csv_lines)
