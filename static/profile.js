

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
        reservation_form: {
            type: '',
            oeuvre: '',
            artiste: '',
            prix: 0,
            adresseLivraison: '',
            commentaire: ''
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
        },
        selectionne_oeuvre: function(oeuvre) {
            console.log("hello oeuvre:", oeuvre)
            this.reservation_form.type = "Réservation";
            this.reservation_form.oeuvre = oeuvre.nom;
            this.reservation_form.artiste = oeuvre.auteur;
        },
        nouvelle_commande: function(artiste) {
            this.reservation_form.type = "Création";
            this.reservation_form.artiste = artiste;
        },
        creer_commande: function () {
            return this.reservation_form.type === "Création" ?
                creer(this.reservation_form) : reserver(this.reservation_form);
        },
        reserver_oeuvre: function() {
            this.creer_commande()
                .then(() => $('#reservation-oeuvre-modal').modal('hide'))
                .catch(err => this.msg = err.message);
        },
    }
})
