<template>
  <div class="dashboard">
    <h1>Área do Cliente</h1>
    <nav>
      <button @click="currentTab = 'status'">Status Implantação</button>
      <button @click="currentTab = 'pagamentos'">Pagamentos</button>
    </nav>
    
    <div class="content">
      <div v-if="currentTab === 'status'">
        <h2>Status da Implantação</h2>
        <p>Acompanhe aqui o progresso...</p>
      </div>
      <div v-if="currentTab === 'pagamentos'">
        <h2>Meus Pagamentos</h2>
        <p>Histórico de faturas...</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentTab: 'status'
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
