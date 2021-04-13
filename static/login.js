async function login(form) {
    return fetch(`/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form)
    });
}

async function regiser(form) {
    return fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form)
    })
}

async function logout() {
    return fetch('/logout', { method: 'POST' });
}

async function devenirArtiste(nom) {
    return fetch('/artiste/devenir', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({nom})
    })
}

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
                .then(()=> window.location.reload());
        },
        onLogin: function (event) {
            event.preventDefault();
            login(this.loginForm)
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
            regiser(this.registerForm).then(res => {
                if (res.status === 201)
                    location.reload();
            })
            this.registerForm.mdpConfirmation = '';
        },
        onLogout: function (event) {
            event.preventDefault();
            logout().then(window.location.reload);
        }
    }
})