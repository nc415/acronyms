from django.shortcuts import render
from lists.models import Society, Acronyms
# Create your views here.
def index(request):
	acronym_list=Acronyms.objects.all().order_by('name')
	print(acronym_list)
	
	context_dict = {'Acronym': acronym_list, }
	
	return render(request, 'emails/index.html', context=context_dict)