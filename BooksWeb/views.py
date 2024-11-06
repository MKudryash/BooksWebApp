from django.http import HttpResponse
from django.shortcuts import render
  
def index(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "index.html", context=data)
 
def about(request):
    return HttpResponse("О сайте")
 
def contact(request):
    return HttpResponse("Контакты")