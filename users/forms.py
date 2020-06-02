from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile
from .countries import COUNTRIES
from django.core.files import File
from PIL import Image
from django import forms


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
    class Meta(UserCreationForm):
        model = CustomUser
        username = None
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        username = None
        fields = ('email',)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        username = None
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    
    nationality = forms.Select(choices=COUNTRIES)
    country_of_residence = forms.Select(choices=COUNTRIES)
    date_of_birth = forms.DateField(widget=forms.TextInput(
        attrs={'type': 'date'}
    ))
    photo = forms.ImageField(label=('Profile Photo'),required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = Profile
        username = None
        fields = [ 'photo', 'first_name', 'last_name', 'nationality', 'country_of_residence', 'date_of_birth', 'sex']
        