from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'second_txt':'help message'}
    return render(request, 'second_app/help.html', context=my_dict)
    