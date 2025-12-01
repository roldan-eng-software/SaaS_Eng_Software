<template>
  <AdminLayout>
    <template #title>Clientes</template>
    
    <div class="mb-6 flex justify-between items-center">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Buscar clientes..."
        class="flex-1 max-w-md px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
      />
      <button
        @click="showModal = true"
        class="ml-4 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors flex items-center"
      >
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
        </svg>
        Novo Cliente
      </button>
    </div>

    <div v-if="loading" class="flex justify-center items-center h-64">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
    </div>

    <div v-else class="bg-white dark:bg-gray-800 rounded-lg shadow overflow-hidden">
      <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
        <thead class="bg-gray-50 dark:bg-gray-700">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Empresa</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">CNPJ</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Telefone</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Data Cadastro</th>
            <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Ações</th>
          </tr>
        </thead>
        <tbody class="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">
          <tr v-for="cliente in filteredClientes" :key="cliente.id" class="hover:bg-gray-50 dark:hover:bg-gray-700">
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900 dark:text-white">
              {{ cliente.nome_empresa }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">
              {{ cliente.cnpj || '-' }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">
              {{ cliente.telefone }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">
              {{ formatDate(cliente.data_cadastro) }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="editCliente(cliente)" class="text-blue-600 hover:text-blue-900 mr-3">Editar</button>
              <button @click="deleteCliente(cliente.id)" class="text-red-600 hover:text-red-900">Excluir</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div v-if="filteredClientes.length === 0" class="text-center py-12 text-gray-500 dark:text-gray-400">
        Nenhum cliente encontrado
      </div>
    </div>

    <div v-if="showModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 w-full max-w-md">
        <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">
          {{ editingCliente ? 'Editar Cliente' : 'Novo Cliente' }}
        </h3>
        <form @submit.prevent="saveCliente">
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Nome da Empresa</label>
            <input v-model="form.nome_empresa" required class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white" />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">CNPJ</label>
            <input v-model="form.cnpj" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white" />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Telefone</label>
            <input v-model="form.telefone" required class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white" />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Endereço</label>
            <textarea v-model="form.endereco" rows="2" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white"></textarea>
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
  name: 'Clientes',
  components: { AdminLayout },
  data() {
    return {
      clientes: [],
      loading: true,
      showModal: false,
      editingCliente: null,
      searchQuery: '',
      form: { nome_empresa: '', cnpj: '', telefone: '', endereco: '', usuario: 1 },
    };
  },
  computed: {
    filteredClientes() {
      if (!this.searchQuery) return this.clientes;
      const query = this.searchQuery.toLowerCase();
      return this.clientes.filter(c =>
        c.nome_empresa.toLowerCase().includes(query) ||
        (c.cnpj && c.cnpj.includes(query))
      );
    },
  },
  mounted() {
    this.loadClientes();
  },
  methods: {
    async loadClientes() {
      try {
        this.loading = true;
        const response = await api.getClientes();
        this.clientes = response.data;
      } catch (error) {
        console.error('Erro ao carregar clientes:', error);
      } finally {
        this.loading = false;
      }
    },
    formatDate(dateString) {
      return new Date(dateString).toLocaleDateString('pt-BR');
    },
    editCliente(cliente) {
      this.editingCliente = cliente;
      this.form = { ...cliente };
      this.showModal = true;
    },
    async saveCliente() {
      try {
        if (this.editingCliente) {
          await api.updateCliente(this.editingCliente.id, this.form);
        } else {
          await api.createCliente(this.form);
        }
        await this.loadClientes();
        this.closeModal();
      } catch (error) {
        console.error('Erro ao salvar cliente:', error);
        alert('Erro ao salvar cliente');
      }
    },
    async deleteCliente(id) {
      if (confirm('Tem certeza que deseja excluir este cliente?')) {
        try {
          await api.deleteCliente(id);
          await this.loadClientes();
        } catch (error) {
          console.error('Erro ao excluir cliente:', error);
        }
      }
    },
    closeModal() {
      this.showModal = false;
      this.editingCliente = null;
      this.form = { nome_empresa: '', cnpj: '', telefone: '', endereco: '', usuario: 1 };
    },
  },
};
</script>
