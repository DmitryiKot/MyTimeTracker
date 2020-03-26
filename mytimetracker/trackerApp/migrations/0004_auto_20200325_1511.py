# Generated by Django 3.0.4 on 2020-03-25 12:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trackerApp', '0003_highleveltask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='highleveltask',
            name='body',
        ),
        migrations.RemoveField(
            model_name='highleveltask',
            name='status',
        ),
        migrations.CreateModel(
            name='LowLevelTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_low', models.CharField(max_length=250)),
                ('slug_low', models.SlugField(max_length=250, unique_for_date='publish_low')),
                ('body', models.TextField()),
                ('publish_low', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_low', models.DateTimeField(auto_now=True)),
                ('created_low', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('close', 'Closed'), ('frozen', 'Frozen')], default='open', max_length=20)),
                ('high_level_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackerApp.HighLevelTask')),
            ],
        ),
    ]
