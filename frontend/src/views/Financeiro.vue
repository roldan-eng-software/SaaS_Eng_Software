<template>
  <AdminLayout>
    <template #title>Financeiro</template>
    
    <div class="mb-6 flex gap-4">
      <select v-model="filterStatus" class="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white">
        <option value="">Todos</option>
        <option value="pendente">Pendentes</option>
        <option value="paga">Pagas</option>
      </select>
      <button @click="showModal = true" class="ml-auto px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 flex items-center">
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
        </svg>
        Nova Fatura
      </button>
    </div>

    <div v-if="loading" class="flex justify-center items-center h-64">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
    </div>

    <div v-else class="bg-white dark:bg-gray-800 rounded-lg shadow overflow-hidden">
      <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
        <thead class="bg-gray-50 dark:bg-gray-700">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Cliente</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Valor</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Vencimento</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Status</th>
            <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Ações</th>
          </tr>
        </thead>
        <tbody class="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">
          <tr v-for="fatura in filteredFaturas" :key="fatura.id" class="hover:bg-gray-50 dark:hover:bg-gray-700">
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 dark:text-white">{{ getClienteNome(fatura.cliente) }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 dark:text-white">R$ {{ formatCurrency(fatura.valor) }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">{{ formatDate(fatura.data_vencimento) }}</td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span :class="fatura.paga ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full">
                {{ fatura.paga ? 'Paga' : 'Pendente' }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button v-if="!fatura.paga" @click="marcarPaga(fatura)" class="text-green-600 hover:text-green-900 mr-3">Marcar Paga</button>
              <button @click="deleteFatura(fatura.id)" class="text-red-600 hover:text-red-900">Excluir</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-if="showModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 w-full max-w-md">
        <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">Nova Fatura</h3>
        <form @submit.prevent="saveFatura">
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Cliente</label>
            <select v-model="form.cliente" required class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white">
              <option value="">Selecione</option>
              <option v-for="cliente in clientes" :key="cliente.id" :value="cliente.id">{{ cliente.nome_empresa }}</option>
            </select>
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Valor</label>
            <input v-model="form.valor" type="number" step="0.01" required class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white" />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Data Vencimento</label>
            <input v-model="form.data_vencimento" type="date" required class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white" />
          </div>
          <div class="flex justify-end gap-3">
            <button type="button" @click="closeModal" class="px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg">Cancelar</button>
            <button type="submit" class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">Salvar</button>
          </div>
        </form>
      </div>
    </div>
  </AdminLayout>
</template>

<script>
import AdminLayout from '../components/AdminLayout.vue';
import api from '../services/api';

export default {
  components: { AdminLayout },
  data() {
    return {
      faturas: [],
      clientes: [],
      loading: true,
      showModal: false,
      filterStatus: '',
      form: { cliente: '', valor: '', data_vencimento: '', paga: false },
    };
  },
  computed: {
    filteredFaturas() {
      if (!this.filterStatus) return this.faturas;
      return this.faturas.filter(f => this.filterStatus === 'paga' ? f.paga : !f.paga);
    },
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      try {
        this.loading = true;
        const [faturasRes, clientesRes] = await Promise.all([api.getFaturas(), api.getClientes()]);
        this.faturas = faturasRes.data;
        this.clientes = clientesRes.data;
      } catch (error) {
        console.error('Erro:', error);
      } finally {
        this.loading = false;
      }
    },
    getClienteNome(id) {
      const cliente = this.clientes.find(c => c.id === id);
      return cliente ? cliente.nome_empresa : '-';
    },
    formatDate(date) {
      return new Date(date).toLocaleDateString('pt-BR');
    },
    formatCurrency(value) {
      return parseFloat(value).toLocaleString('pt-BR', { minimumFractionDigits: 2 });
    },
    async saveFatura() {
      try {
        await api.createFatura(this.form);
        await this.loadData();
        this.closeModal();
      } catch (error) {
        console.error('Erro:', error);
      }
    },
    async marcarPaga(fatura) {
      try {
        await api.updateFatura(fatura.id, { ...fatura, paga: true, data_pagamento: new Date().toISOString().split('T')[0] });
        await this.loadData();
      } catch (error) {
        console.error('Erro:', error);
      }
    },
    async deleteFatura(id) {
      if (confirm('Excluir fatura?')) {
        try {
          await api.deleteFatura(id);
          await this.loadData();
        } catch (error) {
          console.error('Erro:', error);
        }
      }
    },
    closeModal() {
      this.showModal = false;
      this.form = { cliente: '', valor: '', data_vencimento: '', paga: false };
    },
  },
};
</script>
