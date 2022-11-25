from rest_framework import viewsets
from TesteDjangoLibre.models import Professor
from TesteDjangoLibre.serializer import ProfessorSerializer

class ProfessorViewset(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

