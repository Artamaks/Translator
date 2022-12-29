from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def translation(request):
    return render(request, 'translation.html' )