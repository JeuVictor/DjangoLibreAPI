from django.contrib import admin
from TesteDjangoLibre.models import Professor

class Professores(admin.ModelAdmin):
    list_display = ('id','nome','idade', 'sexo', 'materia')
    list_display_links = ('id','nome', 'materia')
    search_fields = ('nome', 'materia',)
# Register your models here.

admin.site.register(Professor, Professores)