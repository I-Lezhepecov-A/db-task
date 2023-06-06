from django.db import models
from datetime import date


class Contract(models.Model):
    name = models.CharField(max_length=128)
    create_date = models.DateField(default=date.today)


class LoanApplication(models.Model):
    name = models.CharField(max_length=128)
    create_date = models.DateField(default=date.today)
    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='loan'
    )


class Item(models.Model):
    name = models.CharField(max_length=128)
    create_date = models.DateField(default=date.today)
    loan = models.ForeignKey(to=LoanApplication, on_delete=models.CASCADE,
                             related_name='items')


class Manufacturer(models.Model):
    name = models.CharField(max_length=128)
    create_date = models.DateField(default=date.today)
    item = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='manufacturer'
    )
