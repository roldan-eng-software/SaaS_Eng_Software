from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render
from django.db.models import Count, Sum, Q
from django.utils import timezone
from datetime import timedelta
from .models import Cliente, Contrato, VisitaTecnica, Fatura, Manutencao, Notificacao
from .serializers import (
    ClienteSerializer, ContratoSerializer, VisitaTecnicaSerializer,
    FaturaSerializer, ManutencaoSerializer, NotificacaoSerializer
)

def landing_page(request):
    """View para renderizar a landing page institucional"""
    return render(request, 'landing.html')

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def dashboard_stats(request):
    """Retorna estatísticas para o dashboard admin"""
    hoje = timezone.now().date()
    mes_atual = hoje.replace(day=1)
    
    # Receita últimos 6 meses
    six_months_ago = hoje - timedelta(days=180)
    revenue_qs = Fatura.objects.filter(
        paga=True,
        data_pagamento__gte=six_months_ago
    ).values('data_pagamento__month').annotate(
        total=Sum('valor')
    ).order_by('data_pagamento__month')
    
    # Formatar dados do gráfico de receita (simplificado)
    revenue_labels = []
    revenue_values = []
    # Map month numbers to names if needed, or just send raw data
    # For simplicity, let's just send the data we have. 
    # In a real app, we'd ensure all 6 months are present even if 0.
    
    stats = {
        'clientes': {
            'total': Cliente.objects.count(),
            'ativos': Contrato.objects.filter(ativo=True).values('cliente').distinct().count(),
            'novos_mes': Cliente.objects.filter(data_cadastro__gte=mes_atual).count(),
        },
        'visitas': {
            'total': VisitaTecnica.objects.count(),
            'pendentes': VisitaTecnica.objects.filter(realizada=False).count(),
            'mes_atual': VisitaTecnica.objects.filter(data_agendada__gte=mes_atual).count(),
        },
        'financeiro': {
            'faturas_pendentes': Fatura.objects.filter(paga=False).count(),
            'valor_pendente': Fatura.objects.filter(paga=False).aggregate(Sum('valor'))['valor__sum'] or 0,
            'valor_recebido_mes': Fatura.objects.filter(
                paga=True, 
                data_pagamento__gte=mes_atual
            ).aggregate(Sum('valor'))['valor__sum'] or 0,
            'receita_total_6_meses': Fatura.objects.filter(
                paga=True, 
                data_pagamento__gte=six_months_ago
            ).aggregate(Sum('valor'))['valor__sum'] or 0,
        },
        'manutencoes': {
            'total': Manutencao.objects.count(),
            'pendentes': Manutencao.objects.filter(concluida=False).count(),
            'proximas_7_dias': Manutencao.objects.filter(
                concluida=False,
                data_programada__gte=hoje,
                data_programada__lte=hoje + timedelta(days=7)
            ).count(),
        },
        'contratos': {
            'ativos': Contrato.objects.filter(ativo=True).count(),
            'total': Contrato.objects.count(),
            'valor_mensal_total': Contrato.objects.filter(ativo=True).aggregate(Sum('valor_mensal'))['valor_mensal__sum'] or 0,
            'pendentes': Contrato.objects.filter(ativo=False).count(), # Aproximação
        },
        'charts': {
            'revenue': list(revenue_qs),
            'projects_status': {
                'concluido': Contrato.objects.filter(ativo=False).count(),
                'em_andamento': Contrato.objects.filter(ativo=True).count(),
                'em_espera': 0, # Placeholder
                'atrasado': Fatura.objects.filter(paga=False, data_vencimento__lt=hoje).count(), # Faturas atrasadas como proxy
            }
        },
        'recent_proposals': list(Contrato.objects.all().order_by('-data_inicio')[:5].values(
            'descricao_sistema', 'cliente__nome_empresa', 'valor_mensal', 'ativo'
        ))
    }
    
    return Response(stats)

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
