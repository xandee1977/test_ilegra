import os
import re


class FileImporter:
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    IN_PATH = 'in/'
    ROW_SEPARATOR = '\n'
    COL_SEPARATOR = ','

    input_filename = None

    def reset_params(self):
        self.file_lines = []
        self.salesmans = []
        self.customers = []
        self.sales = []
        self.top_sale = {"sale_id": None, "value": 0}
        self.worst_salesman = None

    def input_file(self, filename):
        self.input_filename = filename

    def output_path(self, pathname):
        self.output_path = pathname

    # Loads info from file
    def load(self):

        filepath = '{}/{}{}'.format(
            self.BASE_PATH,
            self.IN_PATH,
            self.input_filename
        )
        with open(filepath) as file:
            lines = file.readlines()
        if lines:
            self.file_lines = lines

    # Parse a single line
    def parse_line(self, line):
        # Treats the sale list
        if line.find('[') > 0:
            str1 = line.split('[', 1)[1].split(']')[0]
            str2 = str1.replace(',', '|')
            line = line.replace(str1, str2)
            line = line.replace('[', '').replace(']', '')

        return line.split(self.COL_SEPARATOR)

    def list_items(self, sale_id, sale_data):
        sale_list = []
        sales = sale_data.split('|')

        for sale in sales:
            detail = sale.split('-')
            quantity = int(detail[1])
            price = float(detail[2])

            if price * quantity > self.top_sale['value']:
                self.top_sale['sale_id'] = sale_id
                self.top_sale['value'] = price * quantity

            detail = {
                "id": detail[0],
                "quantity": quantity,
                "price": price
            }
            sale_list.append(detail)

        return sale_list

    # maps the columns meanin
    def map(self, line_fields):
        if line_fields[0] == '001':
            salary = float(line_fields[3].replace('\n', ''))

            data = {
                "type": "salesman",
                "cpf": line_fields[1],
                "name": line_fields[2],
                "salary": salary
            }

            if not self.worst_salesman:
                self.worst_salesman = data
            elif data['salary'] < self.worst_salesman['salary']:
                self.worst_salesman = data

            self.salesmans.append(data)
        elif line_fields[0] == '002':
            data = {
                "type": "customer",
                "cnpj": line_fields[1],
                "name": line_fields[2],
                "area": line_fields[3]
            }
            self.customers.append(data)
        elif line_fields[0] == '003':
            data = {
                "type": "sales",
                "sale_id": line_fields[1],
                "sales": self.list_items(line_fields[1], line_fields[2]),
                "salesman": line_fields[3]
            }
            self.sales.append(data)

    # writes info to output file
    def write(self):
        filepath = '{}/{}{}'.format(
            self.BASE_PATH,
            self.output_path,
            "{}.done.dat".format(self.input_filename)
        )

        file = open(filepath, 'w+')
        file.truncate(0)
        file.write("* Amount of clients: {}\n".format(len(self.salesmans)))
        file.write("* Amount of salesman: {}\n".format(len(self.customers)))
        file.write(
            "* Most expensive sale (ID): {}\n".format(self.top_sale['sale_id'])
        )
        file.write(
            "* Worst salesman ever: {}\n".format(self.worst_salesman['name']))
        file.close()

    def run(self):
        if not self.input_filename:
            return False

        self.reset_params()
        self.load()

        for line in self.file_lines:
            line_fields = self.parse_line(line)
            self.map(line_fields)

        self.write()
