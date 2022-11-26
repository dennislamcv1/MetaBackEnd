from django.contrib import admin
# Import the models from models.py
from .models import Drinks
from .models import DrinksCategory

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinksCategory)