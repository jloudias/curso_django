# Generated by Django 4.2.1 on 2023-05-23 22:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_rename_preparation_dteps_is_html_recipe_preparation_steps_is_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
