<template>
  <AdminLayout>
    <template #title>Visitas Técnicas</template>
    
    <div class="mb-6 flex justify-between items-center">
      <div class="flex-1 max-w-md">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Buscar visitas..."
          class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
        />
      </div>
      <button
        @click="showModal = true"
        class="ml-4 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors flex items-center"
      >
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
        </svg>
        Nova Visita
      </button>
    </div>

    <!-- Loading -->
    <div v-if="loading" class="flex justify-center items-center h-64">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
    </div>

    <!-- Table -->
    <div v-else class="bg-white dark:bg-gray-800 rounded-lg shadow overflow-hidden">
      <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
        <thead class="bg-gray-50 dark:bg-gray-700">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">Cliente</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">Data</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">Motivo</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">Status</th>
            <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">Ações</th>
          </tr>
        </thead>
        <tbody class="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">
          <tr v-for="visita in filteredVisitas" :key="visita.id" class="hover:bg-gray-50 dark:hover:bg-gray-700">
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 dark:text-white">
              {{ getClienteNome(visita.cliente) }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">
              {{ formatDate(visita.data_agendada) }}
            </td>
            <td class="px-6 py-4 text-sm text-gray-500 dark:text-gray-400">
              {{ visita.motivo }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span
                :class="visita.realizada ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'"
                class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full"
              >
                {{ visita.realizada ? 'Realizada' : 'Pendente' }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button
                v-if="!visita.realizada"
                @click="marcarRealizada(visita)"
                class="text-green-600 hover:text-green-900 mr-3"
              >
                Marcar Realizada
              </button>
              <button
                @click="editVisita(visita)"
                class="text-blue-600 hover:text-blue-900 mr-3"
              >
                Editar
              </button>
              <button
                @click="deleteVisita(visita.id)"
                class="text-red-600 hover:text-red-900"
              >
                Excluir
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <div v-if="filteredVisitas.length === 0" class="text-center py-12 text-gray-500 dark:text-gray-400">
        Nenhuma visita encontrada
      </div>
    </div>

    <!-- Modal -->
    <div v-if="showModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 w-full max-w-md">
        <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">
          {{ editingVisita ? 'Editar Visita' : 'Nova Visita' }}
        </h3>
        <form @submit.prevent="saveVisita">
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Cliente</label>
            <select
              v-model="form.cliente"
              required
              class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white"
            >
              <option value="">Selecione um cliente</option>
              <option v-for="cliente in clientes" :key="cliente.id" :value="cliente.id">
                {{ cliente.nome_empresa }}
              </option>
            </select>
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Data</label>
            <input
              v-model="form.data_agendada"
              type="datetime-local"
              required
              class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white"
            />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Motivo</label>
            <textarea
              v-model="form.motivo"
              required
              rows="3"
              class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white"
            ></textarea>
          </div>
          <div class="flex justify-end gap-3">
            <button
              type="button"
              @click="closeModal"
              class="px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg"
            >
              Cancelar
            </button>
            <button
              type="submit"
              class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
            >
              Salvar
            </button>
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
  name: 'VisitasTecnicas',
  components: {
    AdminLayout,
  },
  data() {
    return {
      visitas: [],
      clientes: [],
      loading: true,
      showModal: false,
      editingVisita: null,
      searchQuery: '',
      form: {
        cliente: '',
        data_agendada: '',
        motivo: '',
        realizada: false,
      },
    };
  },
  computed: {
    filteredVisitas() {
      if (!this.searchQuery) return this.visitas;
      const query = this.searchQuery.toLowerCase();
      return this.visitas.filter(v =>
        this.getClienteNome(v.cliente).toLowerCase().includes(query) ||
        v.motivo.toLowerCase().includes(query)
      );
    },
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      try {
        this.loading = true;
        const [visitasRes, clientesRes] = await Promise.all([
          api.getVisitas(),
          api.getClientes(),
        ]);
        this.visitas = visitasRes.data;
        this.clientes = clientesRes.data;
      } catch (error) {
        console.error('Erro ao carregar dados:', error);
      } finally {
        this.loading = false;
      }
    },
    getClienteNome(clienteId) {
      const cliente = this.clientes.find(c => c.id === clienteId);
      return cliente ? cliente.nome_empresa : 'Cliente não encontrado';
    },
    formatDate(dateString) {
      return new Date(dateString).toLocaleString('pt-BR');
    },
    editVisita(visita) {
      this.editingVisita = visita;
      this.form = {
        cliente: visita.cliente,
        data_agendada: visita.data_agendada.slice(0, 16),
        motivo: visita.motivo,
        realizada: visita.realizada,
      };
      this.showModal = true;
    },
    async saveVisita() {
      try {
        if (this.editingVisita) {
          await api.updateVisita(this.editingVisita.id, this.form);
        } else {
          await api.createVisita(this.form);
        }
        await this.loadData();
        this.closeModal();
      } catch (error) {
        console.error('Erro ao salvar visita:', error);
        alert('Erro ao salvar visita');
      }
    },
    async marcarRealizada(visita) {
      try {
        await api.updateVisita(visita.id, { ...visita, realizada: true });
        await this.loadData();
      } catch (error) {
        console.error('Erro ao atualizar visita:', error);
      }
    },
    async deleteVisita(id) {
      if (confirm('Tem certeza que deseja excluir esta visita?')) {
        try {
          await api.deleteVisita(id);
          await this.loadData();
        } catch (error) {
          console.error('Erro ao excluir visita:', error);
        }
      }
    },
    closeModal() {
      this.showModal = false;
      this.editingVisita = null;
      this.form = {
        cliente: '',
        data_agendada: '',
        motivo: '',
        realizada: false,
      };
    },
  },
};
</script>
