from __future__ import unicode_literals
from django.db import models   
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator








class User(AbstractUser):
    gender = (
        ("male", '男'),
        ("female", '女')
    )
    phone_reg = RegexValidator(r'^09\d{2}-?\d{3}-?\d{3}$',"Please enter valid Taiwanese phone number.")
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    sex = models.CharField(max_length=10,choices=gender)
    phone = models.CharField(max_length=20, validators=[phone_reg])

    def __str__(self):
        return self.name

 #留言板
# class student(models.Model):
# 	cName = models.CharField(max_length=20, null=False)
	
# 	cAddr = models.CharField(max_length=255,blank=True, default='')
	
# 	def __str__(self):
# 		return self.cName

#作業牆

