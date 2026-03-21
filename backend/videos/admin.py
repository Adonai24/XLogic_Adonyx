from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    list_display = ('titulo','categoria')
    list_filter = ('categoria',)
    search_fields = ('titulo',)
    
    admin.site.site_header = "Panel XLogic Adonyx"
admin.site.site_title = "Admin XLogic"
admin.site.index_title = "Administración del sistema"