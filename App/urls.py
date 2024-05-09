from rest_framework import routers, viewsets
from App.models import Empleado
from App.serializers import EmpleadoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

router = routers.DefaultRouter()
router.register(r'Empleados', EmpleadoViewSet, basename='Empleado')

urlpatterns = router.urls
