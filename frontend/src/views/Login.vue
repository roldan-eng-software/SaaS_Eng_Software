<template>
  <div class="login-container">
    <h1>Login</h1>
    <form @submit.prevent="login">
      <div>
        <label>Usuário:</label>
        <input v-model="username" type="text" required />
      </div>
      <div>
        <label>Senha:</label>
        <input v-model="password" type="password" required />
      </div>
      <button type="submit">Entrar</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      error: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:8000/api/token/', {
          username: this.username,
          password: this.password
        });
        
        const token = response.data.access;
        localStorage.setItem('token', token);
        
        // Decode token to check if admin (optional, for now assume admin login goes to admin)
        // Or just redirect based on username for simplicity if backend doesn't return role
        if (this.username === 'admin') {
          this.$router.push('/admin');
        } else {
          this.$router.push('/client');
        }
      } catch (err) {
        this.error = 'Login falhou. Verifique suas credenciais.';
        console.error(err);
      }
    }
  }
};
</script>

<style scoped>
.login-container {
  max-width: 300px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.error {
  color: red;
}
</style>
