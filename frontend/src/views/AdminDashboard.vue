<template>
  <div class="dashboard">
    <h1>Painel Administrativo</h1>
    <nav>
      <button @click="currentTab = 'visitas'">Visitas Técnicas</button>
      <button @click="currentTab = 'clientes'">Clientes</button>
      <button @click="currentTab = 'financeiro'">Financeiro</button>
      <button @click="currentTab = 'manutencoes'">Manutenções</button>
      <button @click="currentTab = 'notificacoes'">Notificações</button>
    </nav>
    
    <div class="content">
      <div v-if="currentTab === 'visitas'">
        <h2>Agendamentos de Visitas</h2>
        <p>Lista de visitas técnicas...</p>
        <!-- Aqui viria a lista de visitas da API -->
      </div>
      <div v-if="currentTab === 'clientes'">
        <h2>Controle de Clientes</h2>
        <p>Lista de clientes ativos...</p>
      </div>
      <div v-if="currentTab === 'financeiro'">
        <h2>Área Financeira</h2>
        <p>Controle de recebimentos...</p>
      </div>
      <div v-if="currentTab === 'manutencoes'">
        <h2>Agenda de Manutenções</h2>
        <p>Manutenções mensais...</p>
      </div>
      <div v-if="currentTab === 'notificacoes'">
        <h2>Notificações</h2>
        <p>Enviar avisos...</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentTab: 'visitas'
    };
  }
};
</script>

<style scoped>
nav button {
  margin-right: 10px;
  padding: 10px;
  cursor: pointer;
}
.content {
  margin-top: 20px;
  border: 1px solid #eee;
  padding: 20px;
}
</style>
