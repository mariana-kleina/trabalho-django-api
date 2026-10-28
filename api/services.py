from .models import Categoria, Artigo

class CategoriaService:
    @staticmethod
    def criar(nome, descricao=None):
        return Categoria.objects.create(
            nome=nome,
            descricao=descricao
        )

class ArtigoService:
    @staticmethod
    def criar(titulo, conteudo, categoria, ativo=True):
        return Artigo.objects.create(
            titulo=titulo,
            conteudo=conteudo,
            categoria=categoria,
            ativo=ativo
        )