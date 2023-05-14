from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "age", "degree","music", "sport", "read", "board_games")
  prepopulated_fields = {"slug": ("firstname", "music")}

admin.site.register(Member, MemberAdmin)