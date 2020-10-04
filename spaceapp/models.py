from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


# Create your models here.


class QuizDB_Main(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    img_bool = models.BooleanField(default=False)
    img = models.ImageField(upload_to='QuizImages')


class QuizDB_Live(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, null=True)
    DOB = models.CharField(max_length=100, null=True)
    ph_no = models.CharField(max_length=100, null=True)
    desc = models.CharField(
        max_length=100, default="I find life better, and I'm happier, when things are nice and simple.")
    myimg = models.ImageField(
        upload_to="profileimages\\", default='profileimages/default.jpg', null=True)
    points = models.IntegerField(blank=True, default=0)
    child_name = models.CharField(max_length=100, null=True, unique=True)
