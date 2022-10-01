from turtle import ondrag
from django.db import models
from authApp.models.user import User

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    lastChangeDate = models.DateTimeField()
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.user + ' saldo: ' + self.balance 