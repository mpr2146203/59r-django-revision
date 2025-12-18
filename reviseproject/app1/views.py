from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

# Create your views here.

def sample1(request):
    return HttpResponse("hello i am from django ")
