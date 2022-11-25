from rest_framework import serializers
from TesteDjangoLibre.models import Professor

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id','nome','idade', 'sexo', 'materia']
