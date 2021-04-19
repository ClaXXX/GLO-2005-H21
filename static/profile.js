

const profileApp = new Vue({
    el: '#profile',
    data: {
        oeuvreForm: {
            nom: '',
            dateCreation: Date.now(),
            type: '',
            description: '',
            enExposition: false,
        },
        msg: ''
    },
    delimiters: ['[[', ']]'],
    methods: {
        ajouteOeuvre: function (event) {
            event.preventDefault();
            creer_oeuvre(this.oeuvreForm)
                .then(res => {
                    window.location.reload()
                }).catch(err => {
                    this.msg = err.message
                })
        },
        supprimeOeuvre: function (event,auteur,nom) {
            event.preventDefault();
            supprimer_oeuvre(nom, auteur)
                .then(res => {
                    window.location.reload()
                })
        },
        finCompteArti: function(event){
            event.preventDefault();
            fermerArtiste()
                .then(res => {
                    window.location.reload()
                })
        }

    }
})
