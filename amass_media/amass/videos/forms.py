from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Hidden

from amass.forms import fields, widgets
from amass.common.models import Named, ProjectType
from amass.videos.models import Project, Organization

class OrgRegistrationForm(forms.ModelForm):

    class Meta:
        model = Organization

    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            Organization.objects.get(name=name)
        except Organization.DoesNotExist:
            return name
        raise forms.ValidationError("That organization name is already taken. Please choose another name.")

    def clean(self):
        pass

class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'Add Project'))
        super(ProjectForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Project
        fields = ('name', 'budget', 'application_date', 'description') #add types later
        widgets = {
            #'types': forms.CheckboxSelectMultiple,
            'application_date': widgets.BootstrapSplitDateTimeWidget(
                attrs={
                    'date_class': 'datepicker-default',
                    'time_class':'timepicker-default input-timepicker'
                }),
            'description': forms.Textarea(attrs={'class': 'span4'}),
        }
