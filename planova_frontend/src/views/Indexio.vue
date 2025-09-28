<template>
    <div>
        <!-- Header -->
        <header>
            <nav class="container">
                <div class="logo">
                    <a href="/" class="logo-text">Planova</a>
                </div>
                <ul class="nav-links">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#features">Features</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
                <div style="display: flex; align-items: center">
                    <button class="login-btn" @click="handleLogin">
                        Login
                    </button>
                    <div class="hamburger" @click="toggleMenu">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                </div>
            </nav>
        </header>

        <!-- Hero Section -->
        <section class="hero" id="home">
            <img
                src="/indexio/planner-planova.jpg"
                alt="Team working"
                class="hero-bg"
                onerror="console.log('Image failed to load')"
            />
            <div class="hero-overlay"></div>
            <div class="hero-content">
                <h1>Streamline Your Workflow</h1>
                <p>
                    Boost your productivity with our intuitive platform for
                    teams and projects.
                </p>
                <button class="cta-btn" @click="handleCTA">
                    Get Started Free
                </button>
            </div>
        </section>

        <!-- About Section -->
        <section id="about">
            <div class="container">
                <h2>About AppFlow</h2>
                <p>
                    AppFlow is designed to help teams organize projects
                    efficiently and stay on top of tasks. Simple, powerful, and
                    built for modern workflows.
                </p>
            </div>
        </section>

        <!-- Features Section -->
        <section id="features">
            <div class="container">
                <h2>Features</h2>
                <p>
                    Everything you need to manage projects, collaborate with
                    your team, and achieve your goals.
                </p>
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
                        <p>
                            Gain insights from smart analytics to make
                            data-driven decisions.
                        </p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🔒</div>
                        <h3>Secure</h3>
                        <p>
                            Enterprise-grade security keeps your data safe and
                            private.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact">
            <div class="container">
                <h2>Contact Us</h2>
                <p>
                    Reach out to learn more or get support for your team. We're
                    here to help you succeed.
                </p>
            </div>
        </section>

        <!-- Footer -->
        <footer>
            <div class="container">
                <p>&copy; 2025 AppFlow. All rights reserved.</p>
                <p>
                    <a href="#">Terms</a> | <a href="#">Privacy</a> |
                    <a href="#">Contact</a>
                </p>
            </div>
        </footer>
    </div>
</template>

<script>
export default {
    name: "AppFlow",
    data() {
        return {
            menuOpen: false,
        };
    },
    mounted() {
        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
            anchor.addEventListener("click", function (e) {
                e.preventDefault();
                const target = document.querySelector(
                    this.getAttribute("href"),
                );
                if (target) {
                    target.scrollIntoView({
                        behavior: "smooth",
                        block: "start",
                    });
                }
            });
        });
    },
    methods: {
        handleCTA() {
            alert("Welcome to AppFlow! 🚀");
        },
        handleLogin() {
            alert("Login functionality coming soon!");
        },
        toggleMenu() {
            this.menuOpen = !this.menuOpen;
            alert("Mobile menu toggle");
        },
    },
};
</script>

<style>
@import "../assets/css/indexio/indexio.css";
</style>
