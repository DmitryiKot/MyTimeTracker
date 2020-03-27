from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    about_me = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Profile for {}".format(self.user.username)


class HighLevelTask(models.Model):
    TASK_TYPE = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    finish_date = models.DateTimeField()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=20,
                                 choices=TASK_TYPE,
                                 default='active')

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='user_task')
    objects = models.Manager()

    def get_year(self):
        return self.finish_date.year

    def get_month(self):
        return self.finish_date.month

    def get_day(self):
        return self.finish_date.day

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('trackerApp:high_level_task_details',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class LowLevelTask(models.Model):
    STATUS_TASK = (
        ('open', 'Open'),
        ('close', 'Closed'),
        ('frozen', 'Frozen'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')

    high_level_task = models.ForeignKey(HighLevelTask,
                                        on_delete=models.CASCADE,
                                        related_name='high_task')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=20,
                              choices=STATUS_TASK,
                              default='open')

    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('trackerApp:low_level_task_details',
                       args=[self.publish.month,
                             self.publish.day,
                             self.publish.year,
                             self.slug])


class Comment(models.Model):
    task = models.ForeignKey(HighLevelTask,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
