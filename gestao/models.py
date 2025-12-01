from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente_perfil')
    nome_empresa = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20)
    endereco = models.TextField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_empresa

class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contratos')
    descricao_sistema = models.CharField(max_length=255)
    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    data_inicio = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.descricao_sistema} - {self.cliente.nome_empresa}"

class VisitaTecnica(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='visitas')
    data_agendada = models.DateTimeField()
    motivo = models.TextField()
    realizada = models.BooleanField(default=False)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Visita em {self.data_agendada} - {self.cliente.nome_empresa}"

class Fatura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='faturas')
    contrato = models.ForeignKey(Contrato, on_delete=models.SET_NULL, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    paga = models.BooleanField(default=False)
    data_pagamento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Fatura {self.id} - {self.cliente.nome_empresa}"

class Manutencao(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='manutencoes')
    data_programada = models.DateField()
    descricao = models.TextField()
    concluida = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Manutenção {self.data_programada} - {self.contrato.descricao_sistema}"

class Notificacao(models.Model):
    titulo = models.CharField(max_length=255)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    destinatarios = models.ManyToManyField(Cliente, blank=True, related_name='notificacoes')
    
    def __str__(self):
        return self.titulo
