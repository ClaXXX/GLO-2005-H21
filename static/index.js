// Define a new component called home
Vue.component('home', {
  template: '<li>This is a todo</li>'
})

const vueApp = new Vue({
    el: '#app',
    data: {
      message: `Hello Vue! Random Number: ${Math.random()}`
    },
    delimiters: ['[[', ']]']
})