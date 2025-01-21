# Create your views here.
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

class HomeView(View):
  def get(self, request):
    return render(request, "ui/index.html", {})
