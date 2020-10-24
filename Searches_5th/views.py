from django.shortcuts import render


from .models import SearchQuery


from Days.models import DaysInSearchEngine

# Create your views here.







def search_view(request):
	query = request.GET.get('q', None)
	user = None 
	if request.user.is_authenticated:
		user = request.user
	context = {'query' : query}
	if query is not None:
		SearchQuery.objects.create(user=user, query=query)
		daysinsearchengine = DaysInSearchEngine.objects.search(query=query)    #.all().search()
		context['daysinsearchengine'] = daysinsearchengine
	return render(request, 'Searches/view.html', context)






































