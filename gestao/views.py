from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Cliente, Contrato, VisitaTecnica, Fatura, Manutencao, Notificacao
from .serializers import (
    ClienteSerializer, ContratoSerializer, VisitaTecnicaSerializer,
    FaturaSerializer, ManutencaoSerializer, NotificacaoSerializer
)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Cliente.objects.all()
        return Cliente.objects.filter(usuario=user)

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Contrato.objects.all()
        return Contrato.objects.filter(cliente__usuario=user)

class VisitaTecnicaViewSet(viewsets.ModelViewSet):
    queryset = VisitaTecnica.objects.all()
    serializer_class = VisitaTecnicaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return VisitaTecnica.objects.all()
        return VisitaTecnica.objects.filter(cliente__usuario=user)

class FaturaViewSet(viewsets.ModelViewSet):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Fatura.objects.all()
        return Fatura.objects.filter(cliente__usuario=user)

class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.all()
    serializer_class = ManutencaoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Manutencao.objects.all()
        return Manutencao.objects.filter(contrato__cliente__usuario=user)

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Notificacao.objects.all()
        return Notificacao.objects.filter(destinatarios__usuario=user)
