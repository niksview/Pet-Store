from django.contrib import admin
from .models import Pet 
#@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    lit_display=['id','name','gender','species','breed','age','description']

admin.site.register(Pet,PetAdmin)