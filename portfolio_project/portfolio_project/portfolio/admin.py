# Admin disabled — JSON-only project
# portfolio/admin.py
# Admin disabled (JSON-based project, no models)

from django.contrib import admin
from .models import Profile, Project, ProjectImage, Skill, Experience


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'email')
    search_fields = ('full_name', 'email', 'title')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'featured', 'created_at')
    list_filter = ('featured',)
    search_fields = ('title', 'short_description', 'tech_stack')


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

 

