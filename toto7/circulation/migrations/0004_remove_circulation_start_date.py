# Generated by Django 4.1.5 on 2023-02-02 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulation', '0003_match_tour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circulation',
            name='start_date',
        ),
    ]