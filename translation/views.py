from django.shortcuts import render



# Create your views here.
def translation(request):
    return render(request, 'translation.html' )