<template>
  <div class="d-flex min-vh-100 bg-dark">
    <!-- Sidebar -->
    <aside class="d-flex flex-column flex-shrink-0 p-3 text-white bg-dark border-end border-secondary" style="width: 280px; position: sticky; top: 0; height: 100vh;">
      <div class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none">
        <div class="d-flex align-items-center justify-content-center me-2" style="width: 32px; height: 32px;">
          <svg class="bi me-2" width="32" height="32" fill="#0d6efd" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
            <path d="M44 4H30.6666V17.3334H17.3334V30.6666H4V44H44V4Z" fill="currentColor"></path>
          </svg>
        </div>
        <span class="fs-4 fw-bold">Roldan Eng</span>
      </div>
      <hr>
      <ul class="nav nav-pills flex-column mb-auto">
        <li class="nav-item">
          <router-link to="/admin" class="nav-link text-white" active-class="active">
            <span class="material-symbols-outlined align-middle me-2">dashboard</span>
            Dashboard
          </router-link>
        </li>
        <li>
          <router-link to="/admin/clientes" class="nav-link text-white" active-class="active">
            <span class="material-symbols-outlined align-middle me-2">group</span>
            Clientes
          </router-link>
        </li>
        <li>
          <router-link to="/admin/visitas" class="nav-link text-white" active-class="active">
            <span class="material-symbols-outlined align-middle me-2">event</span>
            Visitas Técnicas
          </router-link>
        </li>
        <li>
          <router-link to="/admin/financeiro" class="nav-link text-white" active-class="active">
            <span class="material-symbols-outlined align-middle me-2">account_balance_wallet</span>
            Financeiro
          </router-link>
        </li>
        <li>
          <router-link to="/admin/manutencoes" class="nav-link text-white" active-class="active">
            <span class="material-symbols-outlined align-middle me-2">build</span>
            Manutenções
          </router-link>
        </li>
        <li>
          <router-link to="/admin/notificacoes" class="nav-link text-white" active-class="active">
            <span class="material-symbols-outlined align-middle me-2">notifications</span>
            Notificações
          </router-link>
        </li>
      </ul>
      <hr>
      <div class="dropdown">
        <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
          <div class="rounded-circle bg-primary d-flex align-items-center justify-content-center me-2" style="width: 32px; height: 32px;">
            <strong>A</strong>
          </div>
          <strong>Admin</strong>
        </a>
        <ul class="dropdown-menu dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser1">
          <li><a class="dropdown-item" href="#">Configurações</a></li>
          <li><a class="dropdown-item" href="#">Perfil</a></li>
          <li><hr class="dropdown-divider"></li>
          <li><a class="dropdown-item" href="#">Sair</a></li>
        </ul>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="flex-grow-1 d-flex flex-column">
      <!-- Top NavBar -->
      <header class="p-3 mb-3 border-bottom border-secondary bg-dark sticky-top">
        <div class="container-fluid d-flex justify-content-between align-items-center">
          <h2 class="h5 mb-0 text-white fw-bold">
            <slot name="title">Dashboard Administrativo</slot>
          </h2>
          
          <div class="d-flex align-items-center">
            <form class="me-3">
              <div class="input-group">
                <span class="input-group-text bg-secondary border-secondary text-light">
                  <span class="material-symbols-outlined fs-6">search</span>
                </span>
                <input type="search" class="form-control bg-dark border-secondary text-white" placeholder="Buscar..." aria-label="Search">
              </div>
            </form>
            
            <div class="d-flex gap-2">
              <button class="btn btn-dark border-secondary text-white">
                <span class="material-symbols-outlined align-middle">notifications</span>
              </button>
              <button class="btn btn-dark border-secondary text-white">
                <span class="material-symbols-outlined align-middle">logout</span>
              </button>
            </div>
          </div>
        </div>
      </header>

      <!-- Page Content -->
      <div class="flex-grow-1 p-4 bg-dark text-white">
        <slot></slot>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'AdminLayout',
};
</script>

<style>
.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}

.nav-pills .nav-link.active, .nav-pills .show > .nav-link {
  background-color: #0d6efd;
}

.nav-link {
  color: #adb5bd;
}

.nav-link:hover {
  color: #fff;
  background-color: rgba(255, 255, 255, 0.1);
}
</style>
