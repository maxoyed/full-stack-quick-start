<template>
  <div id="quick-start">
    <div class="content">{{ message }}</div>
    <div class="content">
      <button @click="fetch_api">Fetch Api</button>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      message: 'Click the button bellow here.'
    }
  },
  methods: {
    fetch_api () {
      this.axios.get('api/hello-world')
        .then(res => {
          console.log(res.data.data)
          this.message = res.data.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
  .content {
    width: 100%;
    display: flex;
    justify-content: space-around;
    align-items: center;
    line-height: 4rem;
    font-size: 1.2rem;
  }
  .content button {
    width: 10vw;
    height: 4vw;
    font-size: 1.2rem;
    border-radius: 4px;
    border: none;
    background: #07c160;
    color: #ffffff;
    outline: none;
    cursor: pointer;
  }
</style>
