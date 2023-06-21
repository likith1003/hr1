from django.contrib import admin
from HR.models import Creds
from HR.models import Student_details,Mock
# Register your models here.
admin.site.register(Creds)
admin.site.register(Student_details)
admin.site.register(Mock)
