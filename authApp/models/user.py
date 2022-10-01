from enum import unique
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

"""
class UserManager(BaseUserManager):
    def create_user(self,username,password):
        user = self.model(username = username)
        user.set_password(password)
        return user
"""

class UserManager(BaseUserManager):
    def create_user(self,username,password=None):
        user = self.model(username = username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username, 
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    def save(self, **kwargs):
        salt = "asdfasdfsfsfsafsafsdfsdffgsfgfdgsfdgh"
        self.password = make_password(self.password,salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
