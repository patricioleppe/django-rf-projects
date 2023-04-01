# routers me permite crear todas las rutas Basicas CRUD
from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects' )

urlpatterns = router.urls