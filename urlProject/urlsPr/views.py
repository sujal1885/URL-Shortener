from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
import random
from .models import Url
import string
from django.contrib import messages
import requests
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def index(request):
    # if this is a POST request we need to process the form data
    # if request.method == 'POST':
        # create a form instance and populate it with data from the request:
       
        # check whether it's valid:
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('Result')

    # if a GET (or any other method) we'll create a blank form

    return render(request, 'index.html')


def createshorturl(request):
    if request.method == 'POST':
        if request.POST['url']=='':
            return redirect('/')
        slug = ''.join(random.choice(string.ascii_letters)for x in range(10))
        url = request.POST["url"]
        new_url = Url(url=url, slug=slug)
        new_url.save()
        return redirect('/Result')

def Result(request):
    url=Url.objects.all()
    last_index = len(url)-1
    req_url = url[last_index].url
    req_slug = url[last_index].slug
    valid = False
    try:
        response = requests.get(req_url)
        if response.status_code == 200:
            valid = True
    except requests.exceptions.RequestException as e:
        valid = False
    return render(request,'Result.html',{'url':url,'last_index':last_index,'req_url':req_url,'req_slug':req_slug,'valid':valid})

def redirect_to_external_site(request, requested_url):
    for url in Url.objects.all():
        if url.slug == requested_url:
          req_url = url.url
          return redirect(f"{req_url}")
    return render(request,'Result.html',{'valid':False})