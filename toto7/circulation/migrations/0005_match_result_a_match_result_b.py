# Generated by Django 4.1.5 on 2023-02-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circulation', '0004_remove_circulation_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='result_a',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='result_b',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]