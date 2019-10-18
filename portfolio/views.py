from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
# Create your views here.

@api_view(['GET'])
def hello(request):
    return HttpResponse("Hello there")


@api_view(['GET'])
def hello_pet(request, pet):
    return HttpResponse("Hello there {}".format(pet))

@api_view(['GET'])
def pets_age(request, y):
    response = y * 7
    return HttpResponse("Your dog's age is {}".format(response))

@api_view(['GET'])
def home(request):
    return render(request, 'home.html')

@api_view(['GET'])
def show_pet(request, pet):
    if not pet:
        pet = None
    return render(request, 'show_pet.html', {'name': pet})

@api_view(['GET'])
def show_home(request, loc):
    if not loc:
        loc = None
    return render(request, 'show_home.html', {'location': loc})

@api_view(['GET'])
def show_skills(request, pet):
    if not pet:
        pet = None
    return render(request, 'show_skills.html', {'name': pet})

@api_view(['GET'])
def food(request, pet):
    return render(request, 'food.html', {'name': pet})

@api_view(['GET'])
def contact(request):
    return render(request, 'contact.html')

@api_view(['GET'])
def about(request):
    return render(request, 'about.html')
