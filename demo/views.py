from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class Another(View):
    def get(self,request):
        return HttpResponse("okok")



def home(reques):
    return HttpResponse("hello")
