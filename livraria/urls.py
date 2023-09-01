from rest_framework import routers
from .views import AutorViewSet, LivrariaViewSet

router = routers.DefaultRouter()
router.register(r'autor', AutorViewSet)
router.register(r'livraria', LivrariaViewSet)
urlpatterns = router.urls