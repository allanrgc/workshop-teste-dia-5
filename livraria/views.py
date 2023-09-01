from rest_framework import viewsets
from .models import Autor, Livraria
from .serializers import AutorSerializer, LivrariaSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivrariaViewSet(viewsets.ModelViewSet):
    queryset = Livraria.objects.all()
    serializer_class = LivrariaSerializer
