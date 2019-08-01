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
def hello_calculate(request, y):
    response = y * 7
    return HttpResponse("Your dog's age is {}".format(response))


@api_view(['GET'])
def show_them(request, pet):
    if not pet:
        pet = None
    return render(request, 'show_them.html', {'name': pet})


@api_view(['GET'])
def food(request, pet):
    return render(request, 'food.html')

@api_view(['GET'])
def contact(request, pet):
    return render(request, 'contact.html')

@api_view(['GET'])
def about(request, pet):
    return render(request, 'about.html')
