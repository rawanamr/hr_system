from django import forms
import logging

from django.contrib import admin
from main.models import Candidates

logger = logging.getLogger('django')




class DateInput(forms.DateInput):
    input_type = 'date'


class RegistrationForm(forms.ModelForm):
    """
          Form for Registration
    """

    class Meta:
        model = Candidates
        fields = ['full_name', 'date_of_birth', 'years_of_experience',
                  'department', 'resume']
        widgets = {
            'date_of_birth': DateInput(),
        }
