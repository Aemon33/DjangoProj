from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'budget','status']
    list_filter = ['budget','status', 'startDate','endDate']
    search_fields  = ['name','budget', 'startDate','endDate']
    show_facets = admin.ShowFacets.ALWAYS
