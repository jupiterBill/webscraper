import requests
from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
def index(request):
    return render(request, template_name= 'base.html')
def new_search(request):
    search = request.POST["search"]
    context = {
        "search": search
    }
    print(search)
    return render(request, "craigslist/new_search.html",context)
# Create your views here.
