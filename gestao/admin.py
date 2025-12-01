from django.contrib import admin
from .models import Cliente, Contrato, VisitaTecnica, Fatura, Manutencao, Notificacao

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome_empresa', 'cnpj', 'telefone', 'data_cadastro']
    search_fields = ['nome_empresa', 'cnpj', 'telefone']
    list_filter = ['data_cadastro']
    ordering = ['-data_cadastro']

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ['descricao_sistema', 'cliente', 'valor_mensal', 'data_inicio', 'ativo']
    search_fields = ['descricao_sistema', 'cliente__nome_empresa']
    list_filter = ['ativo', 'data_inicio']
    ordering = ['-data_inicio']

@admin.register(VisitaTecnica)
class VisitaTecnicaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'data_agendada', 'motivo', 'realizada']
    search_fields = ['cliente__nome_empresa', 'motivo']
    list_filter = ['realizada', 'data_agendada']
    ordering = ['-data_agendada']

@admin.register(Fatura)
class FaturaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'valor', 'data_vencimento', 'paga', 'data_pagamento']
    search_fields = ['cliente__nome_empresa']
    list_filter = ['paga', 'data_vencimento']
    ordering = ['-data_vencimento']

@admin.register(Manutencao)
class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ['contrato', 'data_programada', 'descricao', 'concluida']
    search_fields = ['contrato__descricao_sistema', 'descricao']
    list_filter = ['concluida', 'data_programada']
    ordering = ['-data_programada']

@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_envio']
    search_fields = ['titulo', 'mensagem']
    list_filter = ['data_envio']
    ordering = ['-data_envio']
