from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from clients.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserUpdateModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('is_active',)


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'fio')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()