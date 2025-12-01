<template>
  <AdminLayout>
    <template #title>Manutenções</template>
    
    <div class="mb-6 flex justify-end">
      <button @click="showModal = true" class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 flex items-center">
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
        </svg>
        Nova Manutenção
      </button>
    </div>

    <div v-if="loading" class="flex justify-center items-center h-64">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
    </div>

    <div v-else class="bg-white dark:bg-gray-800 rounded-lg shadow overflow-hidden">
      <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
        <thead class="bg-gray-50 dark:bg-gray-700">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Contrato</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Data</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Descrição</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Status</th>
            <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Ações</th>
          </tr>
        </thead>
        <tbody class="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">
          <tr v-for="manutencao in manutencoes" :key="manutencao.id" class="hover:bg-gray-50 dark:hover:bg-gray-700">
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 dark:text-white">{{ getContratoNome(manutencao.contrato) }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">{{ formatDate(manutencao.data_programada) }}</td>
            <td class="px-6 py-4 text-sm text-gray-500 dark:text-gray-400">{{ manutencao.descricao }}</td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span :class="manutencao.concluida ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full">
                {{ manutencao.concluida ? 'Concluída' : 'Pendente' }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button v-if="!manutencao.concluida" @click="marcarConcluida(manutencao)" class="text-green-600 hover:text-green-900 mr-3">Concluir</button>
              <button @click="deleteManutencao(manutencao.id)" class="text-red-600 hover:text-red-900">Excluir</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-if="showModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 w-full max-w-md">
        <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">Nova Manutenção</h3>
        <form @submit.prevent="saveManutencao">
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Contrato</label>
            <select v-model="form.contrato" required class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white">
              <option value="">Selecione</option>
              <option v-for="contrato in contratos" :key="contrato.id" :value="contrato.id">{{ contrato.descricao_sistema }}</option>
            </select>
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Data</label>
            <input v-model="form.data_programada" type="date" required class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white" />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Descrição</label>
            <textarea v-model="form.descricao" required rows="3" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white"></textarea>
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
      manutencoes: [],
      contratos: [],
      loading: true,
      showModal: false,
      form: { contrato: '', data_programada: '', descricao: '', concluida: false },
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      try {
        this.loading = true;
        const [manutencoesRes, contratosRes] = await Promise.all([api.getManutencoes(), api.getContratos()]);
        this.manutencoes = manutencoesRes.data;
        this.contratos = contratosRes.data;
      } catch (error) {
        console.error('Erro:', error);
      } finally {
        this.loading = false;
      }
    },
    getContratoNome(id) {
      const contrato = this.contratos.find(c => c.id === id);
      return contrato ? contrato.descricao_sistema : '-';
    },
    formatDate(date) {
      return new Date(date).toLocaleDateString('pt-BR');
    },
    async saveManutencao() {
      try {
        await api.createManutencao(this.form);
        await this.loadData();
        this.closeModal();
      } catch (error) {
        console.error('Erro:', error);
      }
    },
    async marcarConcluida(manutencao) {
      try {
        await api.updateManutencao(manutencao.id, { ...manutencao, concluida: true });
        await this.loadData();
      } catch (error) {
        console.error('Erro:', error);
      }
    },
    async deleteManutencao(id) {
      if (confirm('Excluir manutenção?')) {
        try {
          await api.deleteManutencao(id);
          await this.loadData();
        } catch (error) {
          console.error('Erro:', error);
        }
      }
    },
    closeModal() {
      this.showModal = false;
      this.form = { contrato: '', data_programada: '', descricao: '', concluida: false };
    },
  },
};
</script>
