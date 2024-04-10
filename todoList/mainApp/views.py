from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def todos(request):
    return render(request, 'todos.html')

def about(request):
    return render(request, 'about.html')