import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import LandingPage from '../views/LandingPage.vue'
import AdminLayout from '../components/AdminLayout.vue'
import AdminDashboard from '../views/AdminDashboard.vue'
import ClientDashboard from '../views/ClientDashboard.vue'
import VisitasTecnicas from '../views/VisitasTecnicas.vue'
import Clientes from '../views/Clientes.vue'
import Financeiro from '../views/Financeiro.vue'
import Manutencoes from '../views/Manutencoes.vue'
import Notificacoes from '../views/Notificacoes.vue'

const routes = [
    { path: '/', component: LandingPage },
    { path: '/login', component: Login },
    {
        path: '/admin',
        component: AdminDashboard,
        meta: { requiresAuth: true }
    },
    { path: '/client', component: ClientDashboard },
    // Rotas aninhadas ou separadas para admin
    { path: '/admin/visitas', component: VisitasTecnicas },
    { path: '/admin/clientes', component: Clientes },
    { path: '/admin/financeiro', component: Financeiro },
    { path: '/admin/manutencoes', component: Manutencoes },
    { path: '/admin/notificacoes', component: Notificacoes },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
