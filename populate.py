import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emails.settings')

import django
django.setup()
from lists.models import Society, University, Acronym
from datetime import datetime
import csv 

with open('camb.csv', 'r') as csvfile:
	societyreader=csv.reader(csvfile, delimiter=',', quotechar='|')
	
	for row in societyreader:
		
		print (row[0])

		def populate():

			society1 = add_society(society_name=row[0], society_acronym=row[1], society_email=row[2], society_email_status=row[3] )
			

		def add_society(society_name, society_acronym, society_email, society_email_status ) :
			try:
				Uni=University.objects.get(pk=4)
				print (society_email_status)
				c=Society.objects.get_or_create(society_name=society_name, society_acronym=society_acronym, society_email=society_email ,  university=Uni, society_email_status=society_email_status)[0]
				return c
			except:
				pass


		if __name__ == '__main__':
			print("Starting population script")
			populate()

with open('cambacronyms.csv', 'r') as csvfile:
	acronymreader=csv.reader(csvfile, delimiter=',', quotechar='|')

	for row in acronymreader:
		print (row[0])

		def acronympopulate():
			society2=add_acronym(name=row[0])
		def add_acronym(name):
			try:
				d=Acronym.objects.get_or_create(name=name)
				return d
			except:
				pass

			if __name__ =='__main__'
			print ("New Acronym")
			populate()
