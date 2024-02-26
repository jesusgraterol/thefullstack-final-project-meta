from django.contrib.admin import site
from .models import Booking, Menu

# Register your models here.
site.register(Booking)
site.register(Menu)