from django.contrib import admin
from . models import post_model
# Register your models here.

admin.site.site_header = "Django Blog website"
admin.site.site_title = "Django Blog website"
admin.site.index_title = ''

class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title','created_date',)
    list_filter = ('author','title','created_date',)

admin.site.register(post_model,PostAdmin)
