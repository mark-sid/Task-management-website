from django import forms
from .models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }
    def __init__(self, *args, **kwargs):
        self.project = kwargs.pop('project', None)
        super(TaskCreateForm, self).__init__(*args, **kwargs)


    def save(self, commit=True):
        task = super(TaskCreateForm, self).save(commit=False)
        task.project = self.project
        if commit:
            task.save()
        return task


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }