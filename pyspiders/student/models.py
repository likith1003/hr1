from django.db import models

# Create your models here.
class Student_creds(models.Model):
    un=models.CharField(("Username"), max_length=50)
    pw=models.CharField(("Password"), max_length=50)
    pno=models.CharField(("pno"), max_length=50)
