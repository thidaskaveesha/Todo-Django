from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from .forms import TodoForm
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, 'home.html')

def todos(request):
    todos = TodoItem.objects.all()
    form = TodoForm(request.POST or None) # Create a form instance and populate it with data from the request
    if request.method == 'POST':
        if form.is_valid():
            # Extract data from the form
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
        
            # Create a new instance of your model and save it to the database
            TodoItem.objects.create(title=title, description=description)
            return redirect('todos')  # Redirect to the same page after adding the item
    return render(request, 'todos.html', {'form': form, 'todos': todos})

def delete_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)
    todo.delete()
    return redirect('todos')

def cancelBtn(request):
    return redirect('todos')

def about(request):
    return render(request, 'about.html')
