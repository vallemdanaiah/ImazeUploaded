from django.contrib import admin
from .models import Imaze
# Register your models here.
@admin.register(Imaze)   #this 3 lines of code is create id number and object and date also
class ImazeAdmin(admin.ModelAdmin):
    list_display = ['id','photo','date']
#admin.site.register(Imaze)  --->this code give the only imazes