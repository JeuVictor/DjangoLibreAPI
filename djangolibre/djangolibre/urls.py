from django.contrib import admin
from django.urls import path, include
from TesteDjangoLibre.views import ProfessorViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Professores', ProfessorViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path( '', include(router.urls)),
]
