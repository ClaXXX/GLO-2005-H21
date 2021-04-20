const commandesApp = new Vue({
    el: '#commandes',
    delimiters: ['[[', ']]'],
    data: {
        commandes: [],
        commande_artiste: [],
        selected: {undefined},
        commentaire: '',
        commentaires: [],
        msg: ''
    },
    mounted: function () {
        this.mes_commandes()
            .then(num_commande => this.commentaires_par_commande(num_commande));
    },
    methods: {
        change_tab: function (tt) {
            this.commentaires = [];
            if (tt)
                this.mes_commandes()
                    .then(num_commande => this.commentaires_par_commande(num_commande));
            else
                this.commandes_artiste()
                    .then(num_commande => this.commentaires_par_commande(num_commande));

        },
        mes_commandes: async function () {
            this.commandes = await fetch_commandes();
            if (this.commandes.length > 0) {
                this.selected = this.commandes[0];
            }
            return this.selected.num || undefined;
        },
        commandes_artiste: async function () {
            this.commande_artiste = await fetch_artiste_commandes();
            console.log(this.commande_artiste.length)
            this.selected = {};
            if (this.commande_artiste.length > 0) {
                this.selected = this.commande_artiste[0];
            }
            return this.selected.num || undefined;
        },
        commentaires_par_commande: async function (num) {
            this.commentaires = await fetch_commentaires(num);
        },
        selectionner_commande: function (commande) {
            this.selected = commande;
            this.commentaires_par_commande(commande.num);
        },
        ajoute_commentaire: function () {
            if (this.selected.num === undefined)
                return;
            ajoute_commentaire(this.selected.num, this.commentaire).then(() => {
                this.commentaire = '';
                return this.commentaires_par_commande(this.selected.num);
            }).catch(err => this.msg = err.message );
        }
    }
});