from django.shortcuts import render
import requests
# Create your views here.
def movie_list(request):
	query=request.GET.get("q")
	url=  'http://www.omdbapi.com/?apikey=5756839d&s=django' 
	if query:
		url =  'http://www.omdbapi.com/?apikey=5756839d&s=' + query

	response = requests.get(url)

	context = {
		"movies": response.json()
	}

	return render(request,'movies_list.html',context)

def movie_detail(request,movie_id):
	url = 'http://www.omdbapi.com/?&apikey=5756839d&i=' + movie_id
	response = requests.get(url)

	context = {
		"movies": response.json()
	}

	return render(request,'movies_detail.html',context)
