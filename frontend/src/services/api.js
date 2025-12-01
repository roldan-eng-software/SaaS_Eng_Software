import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/api',
    headers: {
        'Content-Type': 'application/json',
    },
});

// Interceptor para adicionar token de autenticação (quando implementado)
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// Serviços da API
export default {
    // Dashboard
    getDashboardStats() {
        return api.get('/dashboard/stats/');
    },

    // Clientes
    getClientes() {
        return api.get('/clientes/');
    },
    getCliente(id) {
        return api.get(`/clientes/${id}/`);
    },
    createCliente(data) {
        return api.post('/clientes/', data);
    },
    updateCliente(id, data) {
        return api.put(`/clientes/${id}/`, data);
    },
    deleteCliente(id) {
        return api.delete(`/clientes/${id}/`);
    },

    // Contratos
    getContratos() {
        return api.get('/contratos/');
    },
    getContrato(id) {
        return api.get(`/contratos/${id}/`);
    },
    createContrato(data) {
        return api.post('/contratos/', data);
    },
    updateContrato(id, data) {
        return api.put(`/contratos/${id}/`, data);
    },
    deleteContrato(id) {
        return api.delete(`/contratos/${id}/`);
    },

    // Visitas Técnicas
    getVisitas() {
        return api.get('/visitas/');
    },
    getVisita(id) {
        return api.get(`/visitas/${id}/`);
    },
    createVisita(data) {
        return api.post('/visitas/', data);
    },
    updateVisita(id, data) {
        return api.put(`/visitas/${id}/`, data);
    },
    deleteVisita(id) {
        return api.delete(`/visitas/${id}/`);
    },

    // Faturas
    getFaturas() {
        return api.get('/faturas/');
    },
    getFatura(id) {
        return api.get(`/faturas/${id}/`);
    },
    createFatura(data) {
        return api.post('/faturas/', data);
    },
    updateFatura(id, data) {
        return api.put(`/faturas/${id}/`, data);
    },
    deleteFatura(id) {
        return api.delete(`/faturas/${id}/`);
    },

    // Manutenções
    getManutencoes() {
        return api.get('/manutencoes/');
    },
    getManutencao(id) {
        return api.get(`/manutencoes/${id}/`);
    },
    createManutencao(data) {
        return api.post('/manutencoes/', data);
    },
    updateManutencao(id, data) {
        return api.put(`/manutencoes/${id}/`, data);
    },
    deleteManutencao(id) {
        return api.delete(`/manutencoes/${id}/`);
    },

    // Notificações
    getNotificacoes() {
        return api.get('/notificacoes/');
    },
    getNotificacao(id) {
        return api.get(`/notificacoes/${id}/`);
    },
    createNotificacao(data) {
        return api.post('/notificacoes/', data);
    },
    updateNotificacao(id, data) {
        return api.put(`/notificacoes/${id}/`, data);
    },
    deleteNotificacao(id) {
        return api.delete(`/notificacoes/${id}/`);
    },
};
