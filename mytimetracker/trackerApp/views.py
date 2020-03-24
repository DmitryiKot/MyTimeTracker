from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from . import forms
from . import models

# Create your views here.


@login_required
def view_profile(request):
    return render(request, 'profile.html', {'user': request.user,
                                            'profile': request.user.profile})


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


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = forms.UserEditForm(instance=request.user,
                                       data=request.POST)
        profile_form = forms.ProfileEditForm(instance=request.user.profile,
                                             data=request.POST,
                                             files=request.FILES)
        user_form.save()
        profile_form.save()
    else:
        user_form = forms.UserEditForm(instance=request.user)
        profile_form = forms.ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


def all_tasks(request):
    task_list = models.HighLevelTask.objects.all()

    return render(request,
                  'highLevelTask/list.html',
                  {"tasks": task_list})


class TaskListView(LoginRequiredMixin, ListView):
    queryset = models.HighLevelTask.objects.all()
    context_object_name = 'tasks'
    template_name = 'highLevelTask/list.html'


@login_required
def high_level_task_details(request, year, month, day, slug):
    task = get_object_or_404(models.HighLevelTask,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             slug=slug)
    # new_comment = None
    #
    # if request.method == 'POST':
    #     comment_form = forms.CommentForm(request.POST)
    #     if comment_form.is_valid():
    #         new_comment = comment_form.save(commit=False)
    #         new_comment.material = material
    #         new_comment.save()
    #     return redirect(material)
    # else:
    #     comment_form = forms.CommentForm()

    return render(request,
                  'highLevelTask/detail.html',
                  {'task': task})


def create_form(request):
    if request.method == 'POST':
        task_form = forms.HighLevelTaskForm(request.POST)
        if task_form.is_valid():
            new_task = task_form.save(commit=False)
            new_task.author = User.objects.first()
            new_task.slug = new_task.title.replace(" ", "-")
            new_task.save()
            return render(request,
                          'highLevelTask/detail.html',
                          {'task': new_task})
    else:
        task_form = forms.HighLevelTaskForm()
    return render(request, "highLevelTask/create_task.html", {'form': task_form})
