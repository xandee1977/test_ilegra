from classes import FileImporter

importer = FileImporter()
importer.load()
'''
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

IN_PATH = 'in/'
OUT_PATH = 'out/'
IN_FILE = 'in.txt'
OUT_FILE= 'out.txt'
ROW_SEPARATOR = '\n';
COL_SEPARATOR = ','

def load_input():
  filepath = '{}/{}/{}'.format(BASE_PATH, IN_PATH, IN_FILE)
  file = open(filepath)

  lines = []
  for row in file:
    for line in row.split(ROW_SEPARATOR):
      lines.append(line)

  file.close()

  return lines

print(load_input())
'''
