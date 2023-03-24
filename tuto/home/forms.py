from django import forms
from django.contrib.auth.models import User
from .models import Booking,UserProfileInfo

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date' : DateInput
        }

        labels = {
            'p_name' : 'Patient Name',
            'p_phone' : 'Phone number',
            'p_email' : 'E-mail id',
            'doc_name' : 'Doctors Name',
            'booking_date' : 'Booking date'
        }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')