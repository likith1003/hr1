from django.db import models

# Create your models here.
class Creds(models.Model):
    username=models.CharField(("Username"), max_length=50)
    password=models.CharField(("Password"), max_length=50)
    def __str__(self):
        return self.username
    
class Student_details(models.Model):
    name=models.CharField(("name"), max_length=50)
    pno=models.CharField(("pno"), max_length=50)
    email=models.CharField(("email"), max_length=50)
    qual=models.CharField(("qual"), max_length=50)
    stream=models.CharField(("stream"), max_length=50)
    dyop=models.CharField(("dyop"), max_length=50)
    dp=models.CharField(("dp"), max_length=50)
    twp=models.CharField(("twp"), max_length=50)
    tp=models.CharField(("tp"), max_length=50)

class Mock(models.Model):
    name=models.CharField(("name"), max_length=50)
    pno=models.CharField(("pno"), max_length=50)
    email=models.CharField(("email"), max_length=50)
    subject=models.CharField(("subject"), max_length=50)
    comm=models.CharField(("Communication rating"), max_length=50)
    tech=models.CharField(("technical rating"), max_length=50)
    prog=models.CharField(("Programming rating"), max_length=50)
    date=models.CharField(("Conducted on"), max_length=50)
    by=models.CharField(("Conducted by"), max_length=50)
    def __str__(self):
        return self.name
 