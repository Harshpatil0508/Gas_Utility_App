from django.contrib import admin
from .models import ServiceRequest


class MemberAdmin(admin.ModelAdmin):
  list_display = ("type","status")
  
admin.site.register(ServiceRequest, MemberAdmin)
