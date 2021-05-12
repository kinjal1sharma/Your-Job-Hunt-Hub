from django.shortcuts import render
from django.http import HttpRequest 
import pandas as pd
from .scrapedtimes import final
from .scrapedindeed import main
from datetime import datetime

def index(request):
    return render(request, "times_jobs/index.html")

def about(request):
    return render(request,"times_jobs/about.html")

def creators(request):
    return render(request,"times_jobs/creators.html")

def search(request):
    return render(request,"times_jobs/search.html")

def timesjobs(request):
    assert isinstance(request, HttpRequest)
    return render(request, "times_jobs/timesjobs.html",{
        'title':'Web Scraper',
        'year':datetime.now().year,
        
    })
   

def indeed(request):
    assert isinstance(request, HttpRequest)
    return render(request, "times_jobs/indeed.html",{
        'title':'Web Scraper',
        'year':datetime.now().year,
    })
     
   

def adder_page(request):

    if request.method == "POST":   
        post = request.POST["post"]
        location = request.POST["location"]     
        final(post, location)
        a = pd.read_csv("times.csv")
        a.to_html("times_jobs/templates/times_jobs/Table1.html")
        return render(request,'times_jobs/Table1.html')


def page_adder(request):
    
    if request.method == "POST":   
        post = request.POST["post"]
        location = request.POST["location"]     
        main(post, location)
        a = pd.read_csv("indeed.csv")
        a.to_html("times_jobs/templates/times_jobs/Table2.html")
        return render(request,'times_jobs/Table2.html')
   