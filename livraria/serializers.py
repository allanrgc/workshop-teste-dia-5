from rest_framework import serializers
from .models import Autor, Livraria

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LivrariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livraria
        fields = '__all__'