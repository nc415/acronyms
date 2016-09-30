import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emails.settings')

import django
django.setup()
from lists.models import Society, University, Acronyms
from datetime import datetime
import csv 



with open('cambacronyms.csv', 'r') as csvfile:
	acronymreader=csv.reader(csvfile, delimiter=',', quotechar='|')

	for row in acronymreader:
		print(row[0])

		def acronympopulate():
			society2=add_acronym(name=row[0], name_only=row[1])
		def add_acronym(name, name_only):
		
			d=Acronyms.objects.get_or_create(name=name, name_only=name_only)
			return d
		
		if __name__ =='__main__':
			print ("New Acronym")
			acronympopulate()
