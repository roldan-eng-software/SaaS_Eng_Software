<template>
  <AdminLayout>
    <template #title>Dashboard Administrativo</template>
    
    <div class="d-flex justify-content-center align-items-center" style="height: 400px;" v-if="loading">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <div v-else>
      <div class="d-flex justify-content-between align-items-center mb-4">
        <h3 class="h3 text-white fw-bold">Visão Geral</h3>
        <!-- ButtonGroup -->
        <div class="d-flex gap-2">
          <button class="btn btn-secondary d-flex align-items-center fw-bold">
            <span class="text-truncate">Adicionar Cliente</span>
          </button>
          <button class="btn btn-primary d-flex align-items-center fw-bold">
            <span class="material-symbols-outlined me-1">add</span>
            <span class="text-truncate">Novo Projeto</span>
          </button>
        </div>
      </div>
      <!-- Stats -->
      <div class="row g-4 mb-4">
        <div class="col-sm-6 col-xl-3">
          <div class="card bg-dark border-secondary h-100">
            <div class="card-body">
              <p class="card-title text-white fw-medium">Total de Projetos Ativos</p>
              <p class="display-6 fw-bold text-white mb-1">{{ stats.contratos?.ativos || 0 }}</p>
              <p class="card-text text-success fw-medium">+2.5%</p>
            </div>
          </div>
        </div>
        <div class="col-sm-6 col-xl-3">
          <div class="card bg-dark border-secondary h-100">
            <div class="card-body">
              <p class="card-title text-white fw-medium">Faturamento Mensal</p>
              <p class="display-6 fw-bold text-white mb-1">{{ formatCurrency(stats.financeiro?.valor_recebido_mes || 0) }}</p>
              <p class="card-text text-success fw-medium">+15.2%</p>
            </div>
          </div>
        </div>
        <div class="col-sm-6 col-xl-3">
          <div class="card bg-dark border-secondary h-100">
            <div class="card-body">
              <p class="card-title text-white fw-medium">Novos Clientes (Mês)</p>
              <p class="display-6 fw-bold text-white mb-1">{{ stats.clientes?.novos_mes || 0 }}</p>
              <p class="card-text text-success fw-medium">+5.0%</p>
            </div>
          </div>
        </div>
        <div class="col-sm-6 col-xl-3">
          <div class="card bg-dark border-secondary h-100">
            <div class="card-body">
              <p class="card-title text-white fw-medium">Orçamentos Pendentes</p>
              <p class="display-6 fw-bold text-white mb-1">{{ stats.contratos?.pendentes || 0 }}</p>
              <p class="card-text text-danger fw-medium">-3.1%</p>
            </div>
          </div>
        </div>
      </div>
      <!-- Charts -->
      <div class="row g-4 mb-4">
        <div class="col-xl-7">
          <div class="card bg-dark border-secondary h-100">
            <div class="card-body d-flex flex-column">
              <div class="mb-3">
                <p class="card-title text-white fw-medium mb-0">Receita nos Últimos 6 Meses</p>
                <div class="d-flex align-items-baseline gap-2">
                  <p class="h2 fw-bold text-white mb-0">{{ formatCurrency(stats.financeiro?.receita_total_6_meses || 0) }}</p>
                  <p class="text-success fw-medium mb-0">+12%</p>
                </div>
              </div>
              <div class="flex-grow-1 position-relative" style="min-height: 250px;">
                 <Line v-if="revenueChartData" :data="revenueChartData" :options="chartOptions" />
              </div>
            </div>
          </div>
        </div>
        <div class="col-xl-5">
          <div class="card bg-dark border-secondary h-100">
            <div class="card-body d-flex flex-column">
              <div class="mb-3">
                <p class="card-title text-white fw-medium mb-0">Projetos por Status</p>
                <div class="d-flex align-items-baseline gap-2">
                  <p class="h2 fw-bold text-white mb-0">{{ stats.contratos?.total || 0 }} Projetos</p>
                  <p class="text-success fw-medium mb-0">+5%</p>
                </div>
              </div>
              <div class="flex-grow-1 position-relative" style="min-height: 250px;">
                 <Bar v-if="statusChartData" :data="statusChartData" :options="barChartOptions" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Recent Proposals Table -->
      <div class="card bg-dark border-secondary">
        <div class="card-header bg-transparent border-secondary">
          <h3 class="h5 fw-bold text-white mb-0">Orçamentos Recentes</h3>
        </div>
        <div class="card-body p-0">
          <div class="table-responsive">
            <table class="table table-dark table-hover mb-0 align-middle">
              <thead>
                <tr>
                  <th class="py-3 ps-4 text-secondary">Projeto</th>
                  <th class="py-3 text-secondary">Cliente</th>
                  <th class="py-3 text-secondary">Valor</th>
                  <th class="py-3 pe-4 text-secondary">Status</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(proposal, index) in stats.recent_proposals" :key="index">
                  <td class="py-3 ps-4 text-white">{{ proposal.descricao_sistema }}</td>
                  <td class="py-3 text-secondary">{{ proposal.cliente__nome_empresa }}</td>
                  <td class="py-3 text-white">{{ formatCurrency(proposal.valor_mensal) }}</td>
                  <td class="py-3 pe-4">
                    <span 
                      class="badge rounded-pill"
                      :class="proposal.ativo ? 'bg-success bg-opacity-25 text-success' : 'bg-warning bg-opacity-25 text-warning'"
                    >
                      {{ proposal.ativo ? 'Ativo' : 'Pendente' }}
                    </span>
                  </td>
                </tr>
                <tr v-if="!stats.recent_proposals?.length">
                  <td colspan="4" class="py-4 text-center text-secondary">Nenhum orçamento recente.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </AdminLayout>
</template>

<script>
import AdminLayout from '../components/AdminLayout.vue';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  Filler
} from 'chart.js'
import { Line, Bar } from 'vue-chartjs'
import { ref, onMounted, computed } from 'vue';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  Filler
)

export default {
  name: 'AdminDashboard',
  components: {
    AdminLayout,
    Line,
    Bar
  },
  setup() {
    const stats = ref({});
    const loading = ref(true);
    const monthNames = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"];

    const formatCurrency = (value) => {
      return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value);
    };

    const fetchStats = async () => {
      try {
        const token = localStorage.getItem('token');
        if (!token) {
          window.location.href = '/login';
          return;
        }
        
        const response = await fetch('http://localhost:8000/api/dashboard/stats/', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        
        if (response.status === 401 || response.status === 403) {
          localStorage.removeItem('token');
          window.location.href = '/login';
          return;
        }

        if (response.ok) {
          stats.value = await response.json();
        }
      } catch (error) {
        console.error('Erro ao buscar estatísticas:', error);
      } finally {
        loading.value = false;
      }
    };

    onMounted(() => {
      fetchStats();
    });

    const revenueChartData = computed(() => {
      if (!stats.value.charts?.revenue) return null;
      
      const labels = stats.value.charts.revenue.map(item => monthNames[item.data_pagamento__month - 1]);
      const data = stats.value.charts.revenue.map(item => item.total);

      return {
        labels: labels,
        datasets: [
          {
            label: 'Receita',
            backgroundColor: (context) => {
              const ctx = context.chart.ctx;
              const gradient = ctx.createLinearGradient(0, 0, 0, 400);
              gradient.addColorStop(0, 'rgba(19, 127, 236, 0.5)');
              gradient.addColorStop(1, 'rgba(19, 127, 236, 0)');
              return gradient;
            },
            borderColor: '#137fec',
            pointBackgroundColor: '#137fec',
            borderWidth: 3,
            fill: true,
            tension: 0.4,
            data: data
          }
        ]
      }
    });

    const statusChartData = computed(() => {
      if (!stats.value.charts?.projects_status) return null;
      
      const s = stats.value.charts.projects_status;
      return {
        labels: ['Concluído', 'Em Andamento', 'Em Espera', 'Atrasado'],
        datasets: [
          {
            label: 'Projetos',
            backgroundColor: ['#0bda5b', '#137fec', '#fa9f38', '#fa6238'],
            data: [s.concluido, s.em_andamento, s.em_espera, s.atrasado],
            borderRadius: 6,
            barThickness: 40
          }
        ]
      }
    });

    const chartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          mode: 'index',
          intersect: false,
          backgroundColor: '#111a22',
          titleColor: '#fff',
          bodyColor: '#92adc9',
          borderColor: '#324d67',
          borderWidth: 1
        }
      },
      scales: {
        x: {
          grid: { display: false },
          ticks: { color: '#92adc9' }
        },
        y: {
          grid: { color: '#233648' },
          ticks: { color: '#92adc9' }
        }
      }
    };

    const barChartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false }
      },
      scales: {
        x: {
          grid: { display: false },
          ticks: { color: '#92adc9' }
        },
        y: {
          display: false
        }
      }
    };

    return {
      stats,
      loading,
      formatCurrency,
      revenueChartData,
      statusChartData,
      chartOptions,
      barChartOptions
    };
  }
};
</script>

<style>
.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}
</style>