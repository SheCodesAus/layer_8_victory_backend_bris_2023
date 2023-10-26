from django.contrib import admin
from users.models import CustomUser, Skill

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
  pass

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
  pass
