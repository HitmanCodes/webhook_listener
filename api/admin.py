from django.contrib import admin

# Register your models here.
from .models import Webhook

admin.site.register(Webhook)