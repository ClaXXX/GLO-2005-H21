const loginApp = new Vue({
    data: {
        loginForm: {
            courriel: '',
            mdp: '',
        },
        registerForm: {
            courriel: '',
            mdp: '',
            mdpConfirmation: '',
            nom: '',
            prenom: '',
            adresse: ''
        },
        artisteForm: {
            nom: ''
        }
    },
    el: '#artwhale-login',
    delimiters: ['[[', ']]'],
    methods: {
        devientArtiste: function (event) {
            event.preventDefault();
            devenirArtiste(this.artisteForm.nom)
                .then(() => window.location.reload());
        },
        onLogin: function (event) {
            event.preventDefault();
            connection(this.loginForm)
                .then(res => {
                    console.log(res);
                    if (res.status === 200)
                        location.reload();
                });
        },
        onRegister: function (event) {
            event.preventDefault();
            if (this.registerForm.mdp !== this.registerForm.mdpConfirmation)
                return;
            delete this.registerForm.mdpConfirmation;
            creer_compte(this.registerForm).then(res => {
                if (res.status === 201)
                    location.reload();
            })
            this.registerForm.mdpConfirmation = '';
        },
        onLogout: function (event) {
            event.preventDefault();
            deconnection().then(() => window.location.reload());
        }
    }
})