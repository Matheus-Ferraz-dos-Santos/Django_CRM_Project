from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, "CRM/home_page.html")

def main_page(request):
    return render(request, "CRM/main_page.html")
