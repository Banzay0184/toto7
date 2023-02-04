from django.db import models


# Create your models here.

class Ticket(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    win = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Command(models.Model):
    name = models.CharField(max_length=100)
    imag = models.ImageField(upload_to='command_imag')

    def __str__(self):
        return self.name


class Circulation(models.Model):
    end_date = models.DateTimeField(null=True, blank=True)
    end_date_current = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.end_date}'


class Match(models.Model):
    start_data = models.DateTimeField(null=True, blank=True)
    command_a = models.ForeignKey(to=Command, on_delete=models.CASCADE, related_name="command_a")
    command_b = models.ForeignKey(to=Command, on_delete=models.CASCADE, related_name="command_b")
    result_a = models.IntegerField(null=True, blank=True)
    result_b = models.IntegerField(null=True, blank=True)
    winner = models.ForeignKey(to=Command, on_delete=models.CASCADE, related_name="winner", null=True, blank=True)
    tour = models.CharField(max_length=255)
    circulation = models.ForeignKey(to=Circulation, on_delete=models.CASCADE, related_name='circulation')

    def __str__(self):
        return f'{self.command_a} and {self.command_b}'