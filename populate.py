import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emails.settings')

import django
django.setup()
from lists.models import Society, University, Site
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
				Sit=Site.objects.get(pk=1)
				Uni=University.objects.get(pk=5)
				print (society_email_status)
				c=Society.objects.get_or_create(site=Sit, society_name=society_name, society_acronym=society_acronym, society_email=society_email ,  university=Uni, society_email_status=society_email_status, society_contact_status="3")[0]
				return c
			except:
				pass


		if __name__ == '__main__':
			print("Starting population script")
			populate()
