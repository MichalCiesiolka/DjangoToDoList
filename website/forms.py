# Create add task form
from django import forms
from .models import Record


class AddTaskForm(forms.ModelForm):
    task_name = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Task Name", "class": "form-control"}), label="")
    description = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Description", "class": "form-control"}), label="")
    finish_until = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={"placeholder": "Finish Until", "class": "form-control"}), label="")
    created_by = forms.CharField(widget=forms.widgets.HiddenInput(attrs={"placeholder": "Description", "class": "form-control"}), label="")
    # finished_at = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={"placeholder": "Finish At", "class": "form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user", "finished_at")
