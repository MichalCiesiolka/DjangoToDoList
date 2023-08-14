from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import AddTaskForm
from django import forms
import datetime


# Create your views here.
def home(request):
    records = Record.objects.all()

    # If user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect('home')
        else:
            messages.success(request, "An error occurred")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def finished_tasks(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect('home')
        else:
            messages.success(request, "An error occurred")
            return redirect('home')
    else:
        return render(request, 'finished_tasks.html', {'records': records})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have benn logged out")
    return redirect('home')


def list_element(request, pk):
    if request.user.is_authenticated:
        # Show element
        task = Record.objects.get(id=pk)
        return render(request, 'record.html', {'task': task})
    else:
        messages.success(request, "You must be logged in to view the element")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Task Deleted")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete element")
        return redirect('home')


def mark_as_finished(request, pk):
    if request.user.is_authenticated:
        finish_it = Record.objects.get(id=pk)
        finish_it.finished_at = datetime.datetime.now()
        finish_it.save(update_fields=["finished_at"])
        messages.success(request, "Task Finished")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to finish a task")
        return redirect('home')


def add_record(request):
    form = AddTaskForm(request.POST or None, initial={"created_by": request.user.username})
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Task has been added")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to add task")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddTaskForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to update task")
        return redirect('home')
