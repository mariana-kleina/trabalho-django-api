from rest_framework import serializers
from .models import Categoria, Artigo

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nome", "descricao"]

class ArtigoSerializer(serializers.ModelSerializer):
    # Exibição detalhada no GET
    categoria = CategoriaSerializer(read_only=True)
    
    # Envio do ID no POST/PUT/PATCH
    categoria_id = serializers.PrimaryKeyRelatedField(
        source="categoria",
        queryset=Categoria.objects.all(),
        write_only=True
    )

    class Meta:
        model = Artigo
        fields = [
            "id",
            "titulo",
            "conteudo",
            "data_criacao",
            "ativo",
            "categoria",
            "categoria_id",
        ]