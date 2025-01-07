from django.contrib import admin
from .models import CodeSet, File

# Register your models here.

admin.site.register({CodeSet, File})


