

const profileApp = new Vue({
    el: '#profile',
    data: {
        oeuvreForm: {
            nom: '',
            dateCreation: Date.now(),
            type: '',
            description: '',
            enExposition: false
        }
    },
    delimiters: ['[[', ']]'],
    methods: {
        ajouteOeuvre: function (event) {
            event.preventDefault();
            creer_oeuvre(this.oeuvreForm)
                .then(res => {
                    if (res.status === 201)
                        window.location.reload()
                })
        },
        supprimeOeuvre: function (event,auteur,nom) {
            event.preventDefault();
            supprimer_oeuvre(nom, auteur)
                .then(res => {
                    if (res.status === 201)
                        window.location.reload()
                })
        },
        finCompteArti: function(event){
            event.preventDefault();
            fermerArtiste()
                .then(res => {
                    if (res.status === 200)
                        window.location.reload()
                })
        }

    }
})
