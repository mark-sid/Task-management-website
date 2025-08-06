from django import forms
from .models import Project


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'deadline_date']
        widgets = {
            'deadline_date': forms.DateInput(attrs={'type': 'date'})
        }
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ProjectCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        project = super(ProjectCreateForm, self).save(commit=False)
        project.user = self.user
        if commit:
            project.save()
        return project


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'deadline_date']
        widgets = {
            'deadline_date': forms.DateInput(attrs={'type': 'date'})
        }