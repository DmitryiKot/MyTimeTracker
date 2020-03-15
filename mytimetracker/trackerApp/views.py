from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import forms
from . import models

# Create your views here.


@login_required
def view_profile(request):
    return render(request, 'profile.html', {'user': request.user})


def register(request):
    if request.method == 'POST':
        user_form = forms.UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'],
            )
            new_user.save()
            models.Profile.objects.create(user=new_user, )
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = forms.UserRegistrationForm()
    return render(request,
                  'register.html',
                  {'form': user_form})
