from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClienteViewSet, ContratoViewSet, VisitaTecnicaViewSet,
    FaturaViewSet, ManutencaoViewSet, NotificacaoViewSet, landing_page, dashboard_stats
)

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'contratos', ContratoViewSet)
router.register(r'visitas', VisitaTecnicaViewSet)
router.register(r'faturas', FaturaViewSet)
router.register(r'manutencoes', ManutencaoViewSet)
router.register(r'notificacoes', NotificacaoViewSet)

urlpatterns = [
    path('landing/', landing_page, name='landing'),
    path('dashboard/stats/', dashboard_stats, name='dashboard-stats'),
    path('', include(router.urls)),
]
