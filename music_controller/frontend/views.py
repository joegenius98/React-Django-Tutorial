from django.shortcuts import render

# Create your views here.


def index(request, *args, **kwargs):
    print(f"Joseph prints request: {request}")
    return render(request, 'frontend/index.html')
