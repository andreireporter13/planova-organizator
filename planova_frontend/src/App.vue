<template>
  <div id="app">
    <Navbar v-if="!hideLayout" />
    
    <router-view />

    <Footer v-if="!hideLayout" />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import { useRoute } from 'vue-router'
import { computed } from 'vue'

export default {
  components: { Navbar, Footer },
  setup() {
    const route = useRoute()

    const hideLayout = computed(() => route.path === '/login' || route.path === '/')

    return { hideLayout }
  }
}
</script>
