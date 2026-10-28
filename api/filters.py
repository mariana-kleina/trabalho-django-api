import django_filters
from .models import Artigo

class ArtigoFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(field_name="titulo", lookup_expr="icontains")
    categoria = django_filters.NumberFilter(field_name="categoria__id")

    class Meta:
        model = Artigo
        fields = ['titulo', 'categoria', 'ativo']