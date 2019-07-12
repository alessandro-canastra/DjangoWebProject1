"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from .models import Event

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['start_date', 'start_time', 'start_datetime', 'start_month', 'start_year']
        widgets = {
            'start_date': DatePickerInput(),
            'start_time': TimePickerInput(),
            'start_datetime': DateTimePickerInput(),
            'start_month': MonthPickerInput(),
            'start_year': YearPickerInput(),
        }
