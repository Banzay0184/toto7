# Generated by Django 4.1.5 on 2023-02-03 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulation', '0006_circulation_end_date_current'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='draw',
        ),
    ]