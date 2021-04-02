// Define a new component called home
Vue.component('home', {
  template: '<li>This is a todo</li>'
});

const API_URL = '';

async function login(courriel, mdp) {
    return fetch(`${API_URL}/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            courriel,
            mdp
        })
    });
}

const loginApp = new Vue({
    el: '#artwhale-login',
    data: {
        courriel: '',
        mdp: '',
    },
    delimiters: ['[[', ']]'],
    methods: {
        onLogin: function (event) {
            event.preventDefault();
            login(this.courriel, this.mdp).then(res => console.log(res));
        }
    }
})