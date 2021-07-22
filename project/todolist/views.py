from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from todolist.models import TodoList
from todolist.forms import TodoListForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == "POST":
        form = TodoListForm(request.POST or None)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.owner=request.user
            instance.save()
            messages.success(request, ("New Task Has Been Added!"))
        return redirect('todolist')
    else:
        all_tasks = TodoList.objects.filter(owner=request.user)
        paginator= Paginator(all_tasks, 5)
        page= request.GET.get('pg')
        all_tasks=paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})


def contact(request):
    context = {
        'contact_text': " Welcome to Contact Us",
    }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        'about_text': " Welcome to About Us Page",
    }
    return render(request, 'about.html', context)

@login_required
def delete(request, task_id):
    task = TodoList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

@login_required
def complete(request, task_id):
    task = TodoList.objects.get(pk=task_id)
    task.done= True
    task.save()
    return redirect('todolist')

@login_required
def pending(request, task_id):
    task = TodoList.objects.get(pk=task_id)
    task.done= False
    task.save()
    return redirect('todolist')

@login_required
def edit(request, task_id):
    if request.method == "POST":
        task = TodoList.objects.get(pk=task_id)
        form = TodoListForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
              # messages.success(request,('Task Is Updated'))
        return redirect('todolist')
    else:
        task_obj=TodoList.objects.get(pk=task_id)
        return render(request, "edit.html", {'task_obj': task_obj})

