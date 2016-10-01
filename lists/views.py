from django.shortcuts import render
from lists.models import Society, Acronyms, Translation
# Create your views here.
def index(request):
	acronym_list=Acronyms.objects.all().order_by('name')
	print(acronym_list)
	Translation_list=Translation.objects.all().order_by('translation_item')
	context_dict = {'Acronym': acronym_list, 'Translation':Translation_list }
	
	return render(request, 'emails/index.html', context=context_dict)