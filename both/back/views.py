from django.shortcuts import render
from .models import RestaurantDetails, RestaurantAddress
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import messages 


# Create your views here.
def home(request):
	data = RestaurantDetails.objects.all()
	if request.method == 'POST':
		
		searchValue = request.POST['search']
		if searchValue:
			matchResult = RestaurantDetails.objects.filter(cuisines__icontains = searchValue)
			match_count = matchResult.count()
			if matchResult:
				return render(request,'show.html',{'match':matchResult,'count':match_count})
			else:
				messages.error(request, "No Result for given Query, Try Something from Cuisines. Below are the available option.")
		else:
			return HttpResponseRedirect(request,'home.html')
	return render(request, 'home.html', {'data': data})
