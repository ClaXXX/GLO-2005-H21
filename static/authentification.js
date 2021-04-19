const loginApp = new Vue({
    data: {
        loginForm: {
            courriel: '',
            mdp: '',
            msg: ''
        },
        registerForm: {
            courriel: '',
            mdp: '',
            mdpConfirmation: '',
            nom: '',
            prenom: '',
            adresse: '',
            msg: ''
        },
        artisteForm: {
            nom: '',
            msg: ''
        },
        msg: ''
    },
    el: '#artwhale-login',
    delimiters: ['[[', ']]'],
    methods: {
        devientArtiste: function (event) {
            event.preventDefault();
            devenirArtiste(this.artisteForm.nom)
                .then(() => window.location.reload())
                .catch(err => this.artisteForm.msg = err.message);
        },
        onLogin: function (event) {
            event.preventDefault();
            connection(this.loginForm)
                .then(res => {
                    location.reload();
                }).catch(err => this.loginForm.msg = err.message);
        },
        onRegister: function (event) {
            event.preventDefault();
            if (this.registerForm.mdp !== this.registerForm.mdpConfirmation)
                return;
            creer_compte(this.registerForm).then(res => {
                location.reload();
            }).catch(err => this.registerForm.msg = err.message)
        },
        onLogout: function (event) {
            event.preventDefault();
            deconnection().then(() => window.location.href = '/');
        }
    }
})