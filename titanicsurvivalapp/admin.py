from django.contrib import admin

# Register your models here.
from .models import History

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'passenger_class')
    


admin.site.register(History, HistoryAdmin)