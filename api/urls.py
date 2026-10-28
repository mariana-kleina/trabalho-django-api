from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ArtigoViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet, basename="categoria")
router.register(r"artigos", ArtigoViewSet, basename="artigo")

urlpatterns = router.urls