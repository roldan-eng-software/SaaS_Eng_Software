import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login.vue';
import AdminDashboard from '../views/AdminDashboard.vue';
import ClientDashboard from '../views/ClientDashboard.vue';

const routes = [
    { path: '/', redirect: '/login' },
    { path: '/login', component: Login },
    { path: '/admin', component: AdminDashboard },
    { path: '/client', component: ClientDashboard },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
