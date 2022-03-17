from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, "leads/home_page.html")

def main_page(request):
    return render(request, "leads/main_page.html")
