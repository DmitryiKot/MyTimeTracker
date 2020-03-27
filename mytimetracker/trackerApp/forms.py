from django import forms
from django.contrib.auth.models import User

from . import models


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label='Pass',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='repeat',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('bad pass')
        return cd['password2']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('about_me', )


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class HighLevelTaskForm(forms.ModelForm):
    class Meta:
        model = models.HighLevelTask
        fields = ('title', 'finish_date')


class LowLevelTaskForm(forms.ModelForm):
    class Meta:
        model = models.LowLevelTask
        fields = ('title', 'body', 'status', 'high_level_task')


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('name', 'body')
