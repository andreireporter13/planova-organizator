<template>
  <div>
    <!-- Header -->
    <header>
      <nav>
        <div class="logo">AppFlow</div>
        <ul class="nav-links">
          <li><a href="#home">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#features">Features</a></li>
          <li><a href="#pricing">Pricing</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
        <div style="display: flex; align-items: center;">
          <button class="login-btn" @click="handleLogin">Login</button>
          <div :class="['hamburger', { open: menuOpen }]" @click="toggleMenu" style="margin-left: 10px;">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>
      </nav>

      <!-- Mobile Menu -->
      <div class="mobile-menu-container" :class="{ show: menuOpen }">
        <div class="mobile-menu">
          <a href="#home" @click="closeMenu">Home</a>
          <a href="#about" @click="closeMenu">About</a>
          <a href="#projects" @click="closeMenu">Projects</a>
          <a href="#features" @click="closeMenu">Features</a>
          <a href="#pricing" @click="closeMenu">Pricing</a>
          <a href="#contact" @click="closeMenu">Contact</a>
          <a href="#" @click="handleLogin">Login</a>
        </div>
      </div>
    </header>

    <!-- Hero Section -->
    <section class="hero" id="home">
      <h1>Streamline Your Workflow</h1>
      <p>Boost your productivity with our intuitive platform for teams and projects.</p>
      <button class="cta-btn" @click="handleCTA">Get Started Free</button>
    </section>

    <!-- About Section -->
    <section id="about">
      <h2>About AppFlow</h2>
      <p>AppFlow is designed to help teams organize projects efficiently and stay on top of tasks.</p>
    </section>

    <!-- Projects Section -->
    <section id="projects">
      <h2>Our Projects</h2>
      <p>Explore different types of projects managed effortlessly with AppFlow.</p>
    </section>

    <!-- Features Section -->
    <section class="features" id="features">
      <h2>Features</h2>
      <p>Everything you need to manage projects, collaborate with your team, and achieve your goals.</p>
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">⚡</div>
          <h3>Fast Performance</h3>
          <p>Optimized platform to keep up with your workflow.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🤝</div>
          <h3>Team Collaboration</h3>
          <p>Work seamlessly with your team in real-time.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">📊</div>
          <h3>Analytics</h3>
          <p>Gain insights from smart analytics to make data-driven decisions.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🔒</div>
          <h3>Secure</h3>
          <p>Enterprise-grade security keeps your data safe and private.</p>
        </div>
      </div>
    </section>

    <!-- Pricing Section -->
    <section id="pricing">
      <h2>Pricing</h2>
      <p>Simple pricing plans to suit teams of all sizes.</p>
    </section>

    <!-- Contact Section -->
    <section id="contact">
      <h2>Contact Us</h2>
      <p>Reach out to learn more or get support for your team.</p>
    </section>

    <!-- Footer -->
    <footer>
      <p>&copy; 2025 AppFlow. All rights reserved.</p>
      <p>
        <a href="#">Terms</a> | <a href="#">Privacy</a> | <a href="#">Contact</a>
      </p>
    </footer>
  </div>
</template>

<script>
export default {
  name: "Indexio",
  data() {
    return {
      menuOpen: false
    };
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
    closeMenu() {
      this.menuOpen = false;
    },
    handleCTA() {
      alert("CTA button clicked!");
    },
    handleLogin() {
      this.$router.push("/login");
    }
  }
};
</script>

<style scoped>
@import '../assets/css/indexio.css';
</style>