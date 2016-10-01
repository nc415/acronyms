from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from lists.models import University, Society, EmailHistory, Acronyms, Site


# Register your models here.
# Register your models here.
    
class AcronymsAdmin(admin.ModelAdmin):
	list_display=('name','name_only')

class SiteAdmin(admin.ModelAdmin):
	list_display=('site_name',)
class UniversityAdmin(admin.ModelAdmin):
	list_display=('university_name', 'university_acronym', 'rag')
	

#class EmailHistoryAdmin(admin.StackedInline):
	#model=EmailHistory
	#fk_name = 'society'


class SocietyAdmin(admin.ModelAdmin):
	actions = ['download_csv']
	list_filter = (('site','university__university_name', 'society_contact_status', 'society_email_status'))
	list_display=('university', 'society_name', 'society_email', 'society_email_status', 'society_contact_status', 'notes' )
	search_fields = ['society_name', 'society_acronym']
	

	#inlines = [
     #   EmailHistoryAdmin,
    #]

	
	def download_csv(self, request, queryset):
		import csv
		from django.http import HttpResponse
		import StringIO

		f = StringIO.StringIO()
		writer = csv.writer(f)
		writer.writerow(["university", "society_name", "society_acronym", "society_email", "society_email_status", "society_contact_status", "notes" ])

		for s in queryset:
		    writer.writerow([s.university, s.society_name, s.society_acronym, s.society_email, s.society_email_status, s.society_contact_status, s.notes])

		f.seek(0)
		response = HttpResponse(f, content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
		return response
	#code to prepopulate the slug field  when you type in a new category name
admin.site.register(University, UniversityAdmin)
admin.site.register(Society, SocietyAdmin)
admin.site.register(Acronyms, AcronymsAdmin)
admin.site.register(Site, SiteAdmin)
#admin.site.register(EmailHistory, EmailHistoryAdmin)


