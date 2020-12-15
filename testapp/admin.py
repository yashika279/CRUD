from django.contrib import admin
from testapp.models import Insertion
class InsertionAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','salary']
# Register your models here.
admin.site.register(Insertion,InsertionAdmin)
# Register your models here.
