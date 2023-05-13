import requests
from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from . import models
JUMIA_URL = 'https://www.jumia.com.ng/catalog/?q={}'
def index(request):
    return render(request, template_name= 'base.html')
def new_search(request):
    search = request.POST["search"]
    #existing_search = models.Search.objects.filter(search  = search).first()
    #if(existing_search):
    #    print("found", existing_search)
    #else:
    #    models.Search.objects.create(search=search)


    final_url = JUMIA_URL.format(quote_plus(search))
    response = requests.get(final_url).text
    soup = BeautifulSoup(response, features='html.parser')
    detail = []
    if soup.find_all("a",  {'class': 'core'}):
        lsts = soup.find_all("a",  {'class': 'core'})
        for link in lsts:
            if link.find("h3"):
                name = link.find("h3").get_text()
                price =(link.find("div",{"class":"prc"}).get_text())
                image = link.find("div", {'class': 'img-c'}).find("img",{"class":"img"}).get("data-src")
                more_det = link.get("href")
                detail.append((name,price,image,more_det))
            else:
                name = link.find("div",{"class":"name"}).get_text()
                price = link.find("div",{"class":"prc"}).get_text()
                image = link.find("img").get("data-src")
                more_det = link.get("href")
                detail.append((name, price, image, more_det))
    else:
        detail.append(("NOT FOUND TRY ANOTHER SEARCH","N/A","https://img.freepik.com/free-vector/oops-404-error-with-broken-robot-concept-illustration_114360-5529.jpg?w=2000","NOT FOUND TRY ANOTHER SEARCH"))
    print(detail)
    context = {
        "search": search,
        "detail":detail
    }

    return render(request, "craigslist/new_search.html",context)
# Create your views here.
