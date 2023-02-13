from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Ticket(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    win = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Command(models.Model):
    name = models.CharField(max_length=100)
    imag = models.ImageField()

    def __str__(self):
        return self.name


class Circulation(models.Model):
    number = models.IntegerField()
    end_date = models.DateTimeField(null=True, blank=True)
    end_date_current = models.DateTimeField(null=True, blank=True)
    end_date_finish = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.number}'


class Match(models.Model):
    start_data = models.DateTimeField(null=True, blank=True)
    command_a = models.ForeignKey(to=Command, on_delete=models.CASCADE, related_name="command_a")
    command_b = models.ForeignKey(to=Command, on_delete=models.CASCADE, related_name="command_b")
    result_a = models.IntegerField(null=True, blank=True)
    result_b = models.IntegerField(null=True, blank=True)
    winner = models.ForeignKey(to=Command, on_delete=models.CASCADE, related_name="winner", null=True, blank=True)
    tour = models.CharField(max_length=255)
    circulation = models.ForeignKey(to=Circulation, on_delete=models.CASCADE, related_name='circulations')

    def __str__(self):
        return f'{self.command_a} and {self.command_b}'


class User(AbstractUser):
    role = (
        ('ADMIN', 'Админ'),
        ('CLIENT', 'Клиент'),
    )

    image = models.ImageField(null=True, blank=True)
    role = models.CharField(choices=role, max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    region = models.CharField(max_length=150, null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.last_name
