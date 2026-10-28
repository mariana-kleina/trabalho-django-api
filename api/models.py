from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    # PROTECT impede exclusão em cadeia acidental
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="artigos"
    )

    def __str__(self):
        return self.titulo