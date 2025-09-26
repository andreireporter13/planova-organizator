<template>
  <div id="app">
    <main>
      <p>Conținutul paginii...</p>
    </main>

    <footer>
      Footer lipit de jos
    </footer>
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>

<style>
html, body {
  height: 100%;
  margin: 0;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  flex: 1; /* ocupă tot spațiul liber */
}

footer {
  background-color: #42b983;
  color: white;
  text-align: center;
  padding: 15px;
}
</style>
