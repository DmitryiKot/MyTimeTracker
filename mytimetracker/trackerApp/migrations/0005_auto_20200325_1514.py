# Generated by Django 3.0.4 on 2020-03-25 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackerApp', '0004_auto_20200325_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lowleveltask',
            old_name='created_low',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='lowleveltask',
            old_name='publish_low',
            new_name='publish',
        ),
        migrations.RenameField(
            model_name='lowleveltask',
            old_name='slug_low',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='lowleveltask',
            old_name='title_low',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='lowleveltask',
            old_name='updated_low',
            new_name='updated',
        ),
    ]