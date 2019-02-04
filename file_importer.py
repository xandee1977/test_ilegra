import glob

from classes import FileImporter

importer = FileImporter()
#importer.output_parh('%HOMEPATH%/data/out/')
importer.output_path('out/')

for f in glob.glob('in/*'):
	path = f.split('/')
	importer.input_file(path[1])
	importer.run()
