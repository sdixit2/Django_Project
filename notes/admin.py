from django.contrib import admin
from . import models
# Register your models here.

class NodesAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Notes,NodesAdmin)
