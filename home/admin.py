from django.contrib import admin
from home.models import Review, Contact, Doctor

# Register your models here.
admin.site.register((Review,Contact,Doctor))
