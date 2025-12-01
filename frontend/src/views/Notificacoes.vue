<template>
  <AdminLayout>
    <template #title>Notificações</template>
    
    <div class="mb-6 flex justify-end">
      <button @click="showModal = true" class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 flex items-center">
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
        </svg>
        Nova Notificação
      </button>
    </div>

    <div v-if="loading" class="flex justify-center items-center h-64">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
    </div>

    <div v-else class="space-y-4">
      <div v-for="notificacao in notificacoes" :key="notificacao.id" class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <div class="flex justify-between items-start">
          <div class="flex-1">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">{{ notificacao.titulo }}</h3>
            <p class="text-gray-600 dark:text-gray-400 mb-3">{{ notificacao.mensagem }}</p>
            <p class="text-sm text-gray-500 dark:text-gray-500">Enviado em: {{ formatDate(notificacao.data_envio) }}</p>
          </div>
          <button @click="deleteNotificacao(notificacao.id)" class="text-red-600 hover:text-red-900 ml-4">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
          </button>
        </div>
      </div>
      <div v-if="notificacoes.length === 0" class="text-center py-12 text-gray-500 dark:text-gray-400">
        Nenhuma notificação enviada
      </div>
    </div>

    <div v-if="showModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 w-full max-w-md">
        <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">Nova Notificação</h3>
        <form @submit.prevent="saveNotificacao">
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Título</label>
            <input v-model="form.titulo" required class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white" />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Mensagem</label>
            <textarea v-model="form.mensagem" required rows="4" class="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white"></textarea>
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Destinatários</label>
            <div class="space-y-2 max-h-40 overflow-y-auto">
              <label v-for="cliente in clientes" :key="cliente.id" class="flex items-center">
                <input type="checkbox" :value="cliente.id" v-model="form.destinatarios" class="mr-2" />
                <span class="text-sm text-gray-700 dark:text-gray-300">{{ cliente.nome_empresa }}</span>
              </label>
            </div>
          </div>
          <div class="flex justify-end gap-3">
            <button type="button" @click="closeModal" class="px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg">Cancelar</button>
            <button type="submit" class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">Enviar</button>
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
      notificacoes: [],
      clientes: [],
      loading: true,
      showModal: false,
      form: { titulo: '', mensagem: '', destinatarios: [] },
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      try {
        this.loading = true;
        const [notificacoesRes, clientesRes] = await Promise.all([api.getNotificacoes(), api.getClientes()]);
        this.notificacoes = notificacoesRes.data;
        this.clientes = clientesRes.data;
      } catch (error) {
        console.error('Erro:', error);
      } finally {
        this.loading = false;
      }
    },
    formatDate(date) {
      return new Date(date).toLocaleString('pt-BR');
    },
    async saveNotificacao() {
      try {
        await api.createNotificacao(this.form);
        await this.loadData();
        this.closeModal();
      } catch (error) {
        console.error('Erro:', error);
      }
    },
    async deleteNotificacao(id) {
      if (confirm('Excluir notificação?')) {
        try {
          await api.deleteNotificacao(id);
          await this.loadData();
        } catch (error) {
          console.error('Erro:', error);
        }
      }
    },
    closeModal() {
      this.showModal = false;
      this.form = { titulo: '', mensagem: '', destinatarios: [] };
    },
  },
};
</script>
