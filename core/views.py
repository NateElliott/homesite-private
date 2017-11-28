from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from random import randrange

class Root(View):

    def get(self, request):

        return render(request,'index.html')
