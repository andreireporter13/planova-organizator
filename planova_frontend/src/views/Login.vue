<template>
  <div class="auth-container">
    <!-- Background decoration -->
    <div class="bg-decoration">
      <div class="floating-orb orb-1"></div>
      <div class="floating-orb orb-2"></div>
      <div class="floating-orb orb-3"></div>
    </div>

    <div class="auth-wrapper">

      <!-- Glassmorphism card -->
      <div class="auth-card">

        <!-- Branding -->
        <div class="branding">
          <img :src="logo" alt="Logo App" class="logo" />
        </div>

        <!-- Header -->
        <div class="auth-header">
          
          <h2 class="auth-title">
            {{ isLogin ? 'Bine ai revenit!' : 'Creează cont' }}
          </h2>
          <p class="auth-subtitle">
            {{ isLogin ? 'Introdu datele tale pentru a accesa contul' : 'Completează informațiile pentru a începe' }}
          </p>
        </div>

        <!-- Login Form -->
        <div v-if="isLogin" class="form-section">
          <div class="input-group">
            <i class="input-icon icon-user"></i>
            <input
              v-model="loginUser"
              type="text"
              placeholder="Nume utilizator"
              class="form-input"
            />
          </div>

          <div class="input-group">
            <i class="input-icon icon-lock"></i>
            <input
              v-model="loginPass"
              :type="showPassword ? 'text' : 'password'"
              placeholder="Parolă"
              class="form-input"
            />
            <button
              type="button"
              @click="showPassword = !showPassword"
              class="password-toggle"
            >
              <i class="icon" :class="showPassword ? 'icon-eye-off' : 'icon-eye'"></i>
            </button>
          </div>

          <div class="form-options">
            <label class="checkbox-label">
              <input type="checkbox" class="checkbox" />
              <span class="checkbox-text">Ține-mă minte</span>
            </label>
            <a href="#" class="forgot-link">Ai uitat parola?</a>
          </div>

          <button @click="handleLogin" class="auth-button login-btn">
            Autentificare
          </button>
        </div>

        <!-- Register Form -->
        <div v-else class="form-section">
          <div class="input-group">
            <i class="input-icon icon-user"></i>
            <input
              v-model="registerUser"
              type="text"
              placeholder="Nume utilizator"
              class="form-input"
            />
          </div>

          <div class="input-group">
            <i class="input-icon icon-mail"></i>
            <input
              v-model="registerEmail"
              type="email"
              placeholder="Email"
              class="form-input"
            />
          </div>

          <div class="input-group">
            <i class="input-icon icon-lock"></i>
            <input
              v-model="registerPass"
              :type="showPassword ? 'text' : 'password'"
              placeholder="Parolă"
              class="form-input"
            />
            <button
              type="button"
              @click="showPassword = !showPassword"
              class="password-toggle"
            >
              <i class="icon" :class="showPassword ? 'icon-eye-off' : 'icon-eye'"></i>
            </button>
          </div>

          <div class="terms-section">
            <label class="checkbox-label terms-label">
              <input type="checkbox" class="checkbox" />
              <span class="checkbox-text">
                Sunt de acord cu <a href="#" class="terms-link">Termenii și condițiile</a> 
                și <a href="#" class="terms-link">Politica de confidențialitate</a>
              </span>
            </label>
          </div>

          <button @click="handleRegister" class="auth-button register-btn">
            Creează cont
          </button>
        </div>

        <!-- Switch between forms -->
        <div class="switch-section">
          <p class="switch-text">
            {{ isLogin ? "Nu ai cont?" : "Ai deja cont?" }}
            <button
              @click="isLogin = !isLogin"
              class="switch-button"
            >
              {{ isLogin ? "Înregistrează-te" : "Autentificare" }}
            </button>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import logo from '../assets/media/logo.webp'

export default {
  name: "LoginPage",
  setup() {
    const isLogin = ref(true)
    const showPassword = ref(false)

    // login form
    const loginUser = ref("")
    const loginPass = ref("")
    const handleLogin = () => {
      if (loginUser.value && loginPass.value) {
        alert(`Utilizator autentificat: ${loginUser.value}`)
      }
    }

    // register form
    const registerUser = ref("")
    const registerEmail = ref("")
    const registerPass = ref("")
    const handleRegister = () => {
      if (registerUser.value && registerEmail.value && registerPass.value) {
        alert(`Utilizator înregistrat: ${registerUser.value}, Email: ${registerEmail.value}`)
      }
    }

    return {
      isLogin,
      showPassword,
      loginUser,
      loginPass,
      registerUser,
      registerEmail,
      registerPass,
      handleLogin,
      handleRegister,
      logo,
    }
  },
}
</script>

<style scoped>
@import '../assets/css/login.css';
</style>
