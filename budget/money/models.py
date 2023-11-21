from django.db import models


class Remain(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)


class Expense(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    amount = models.FloatField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)


class Income(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    amount = models.FloatField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
