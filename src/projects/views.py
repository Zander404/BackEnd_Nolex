from django.shortcuts import render
import requests, json

# Create your views here.

def index(request):
    response = requests.get(f'https://api.github.com/users/zander404/repos').json()
    return render(request, "index.html", {"data": response})