# Generated by Django 4.1.5 on 2023-02-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circulation', '0009_alter_command_imag'),
    ]

    operations = [
        migrations.AddField(
            model_name='circulation',
            name='end_date_finsh',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='circulation',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]