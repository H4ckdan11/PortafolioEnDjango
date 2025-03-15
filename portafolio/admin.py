from django.contrib import admin
from .models import Portafolio

# Register your models here.
@admin.register(Portafolio)
class PortafolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'url']