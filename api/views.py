from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Categoria, Artigo
from .serializers import CategoriaSerializer, ArtigoSerializer
from .services import ArtigoService
from .filters import ArtigoFilter

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ArtigoViewSet(viewsets.ModelViewSet):
    queryset = Artigo.objects.select_related("categoria").all()
    serializer_class = ArtigoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtigoFilter

    def perform_create(self, serializer):
        ArtigoService.criar(
            titulo=serializer.validated_data["titulo"],
            conteudo=serializer.validated_data["conteudo"],
            categoria=serializer.validated_data["categoria"],
            ativo=serializer.validated_data.get("ativo", True)
        )