# Generated by Django 4.1.6 on 2023-02-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circulation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betinfo',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='circulation',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='win',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]