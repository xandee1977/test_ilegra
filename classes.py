import os

class FileImporter:
  BASE_PATH = os.path.dirname(os.path.abspath(__file__))

  IN_PATH = 'in/'
  OUT_PATH = 'out/'
  IN_FILE = 'in.txt'
  OUT_FILE= 'out.txt'
  ROW_SEPARATOR = '\n';
  COL_SEPARATOR = ','

  file_lines = []

  # Loads info from file
  def load(self):
    filepath = '{}/{}/{}'.format(
      self.BASE_PATH,
      self.IN_PATH,
      self.IN_FILE
    )
    with open(filepath) as file:
      self.file_lines = file.readlines()

  # Parse a single line
  def parse(self, line):
    return line.split(self.COL_SEPARATOR)

  # maps the columns meanin
  def map(self, line_list):
    print('Map the file')

  # writes info to output file
  def write(self):
    print('Write the file')
