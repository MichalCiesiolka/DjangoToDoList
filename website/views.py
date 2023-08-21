from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import SignUpForm, AddTaskForm
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


# def finished_tasks(request):
#     records = Record.objects.all()
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Logged In")
#             return redirect('home')
#         else:
#             messages.success(request, "An error occurred")
#             return redirect('home')
#     else:
#         return render(request, 'finished_tasks.html', {'records': records})

def finished_tasks(request):
    records = Record.objects.all()
    if request.user.is_authenticated:
        return render(request, 'finished_tasks.html', {'records': records})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def list_element(request, pk):
    if request.user.is_authenticated:
        # Show element
        task = Record.objects.get(id=pk)
        return render(request, 'record.html', {'task': task})
    else:
        messages.success(request, "You must be logged in to view the element")
        return redirect('home')


def finished_element(request, pk):
    if request.user.is_authenticated:
        # Show element
        task = Record.objects.get(id=pk)
        return render(request, 'finished_record.html', {'task': task})
    else:
        messages.success(request, "You must be logged in to view the element")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        if request.user.username == delete_it.created_by or request.user.is_superuser:
            delete_it.delete()
            messages.success(request, "Task Deleted")
            return redirect('home')
        else:
            messages.success(request, "You can't remove other users' tasks")
            return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete element")
        return redirect('home')


def mark_as_finished(request, pk):
    if request.user.is_authenticated:
        finish_it = Record.objects.get(id=pk)
        if request.user.username == finish_it.created_by or request.user.is_superuser:
            finish_it.finished_at = datetime.datetime.now()
            finish_it.save(update_fields=["finished_at"])
            messages.success(request, "Task Finished")
            return redirect('home')
        else:
            messages.success(request, "You can't finish other users' tasks")
            return redirect('home')
    else:
        messages.success(request, "You must be logged in to finish a task")
        return redirect('home')


def mark_as_unfinished(request, pk):
    if request.user.is_authenticated:
        finish_it = Record.objects.get(id=pk)
        if request.user.username == finish_it.created_by or request.user.is_superuser:
            finish_it.finished_at = None
            finish_it.save(update_fields=["finished_at"])
            messages.success(request, "Task Restored")
            return redirect('home')
        else:
            messages.success(request, "You can't restore other users' tasks")
            return redirect('home')
    else:
        messages.success(request, "You must be logged in to restore a task")
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


def update_finished_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddTaskForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated")
            return redirect('finished_tasks')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to update task")
        return redirect('finished_tasks')
