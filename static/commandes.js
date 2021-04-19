const commandesApp = new Vue({
    el: '#commandes',
    delimiters: ['[[', ']]'],
    data: {
        commandes: [],
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
        mes_commandes: async function () {
            this.commandes = await fetch_commandes();
            if (this.commandes.length > 0) {
                this.selected = this.commandes[0];
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
            }).catch(err => this.msg = err.message );
        }
    }
});