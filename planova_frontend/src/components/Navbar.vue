<template>
    <nav class="dashboard-navbar">
        <div class="navbar-left">
            <span class="app-name">Planova</span>
        </div>

        <ul :class="['nav-links', { active: isMenuOpen }]">
            <li><a href="#">Acasă</a></li>
            <li><a href="#">Istoric</a></li>
            <li><a href="#">Scraperi</a></li>
            <li><a href="#">Setări</a></li>
        </ul>

        <div class="navbar-right">
            <span class="user-name">Salut, Andrei Cojocaru!</span>
            <button class="logout-btn" @click="handleLogout">Logout</button>
            <button class="burger-btn" @click="toggleMenu">
                <span :class="{ 'burger-open': isMenuOpen }"></span>
                <span :class="{ 'burger-open': isMenuOpen }"></span>
                <span :class="{ 'burger-open': isMenuOpen }"></span>
            </button>
        </div>
    </nav>
</template>

<script>
import { ref } from "vue";

export default {
    name: "DashboardNavbar",
    setup() {
        const isMenuOpen = ref(false);

        const toggleMenu = () => {
            isMenuOpen.value = !isMenuOpen.value;
        };

        const handleLogout = () => {
            alert("Te-ai delogat!");
        };

        return { isMenuOpen, toggleMenu, handleLogout };
    },
};
</script>

<style scoped>
@import "../assets/css/dashboard/dashboard-navbar.css";
</style>
