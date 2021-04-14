const vueApp = new Vue({
    el: '#app',
    data: {
        oeuvres: [
        ],
        artistes: [
        ],
        type_recherche: '',
        recherche:'',
    },
    delimiters: ['[[', ']]'],
    mounted:function(){
            this.auChargement()
        },
    methods: {
        auChargement: async function () {
            artistes = await fetch_artiste()
            galerie = await fetch_oeuvre()
            for(let oeuvre of galerie){
                 this.oeuvres.push({nom: oeuvre.nom, auteur: oeuvre.auteur,dateCreation: oeuvre.dateCreation,type:oeuvre.type,description:oeuvre.desc})
            }
            for(let artiste of artistes){
                this.artistes.push({nom: artiste.nom})
            }
        },
        onSearch: function(event){
            event.preventDefault();
            rechercher(this.recherche,this.type_recherche).then(res => {
                this.oeuvres = res.map(oeuvre => ({nom: oeuvre.nom, auteur: oeuvre.auteur,dateCreation: oeuvre.dateCreation,type:oeuvre.type,description:oeuvre.desc}))
                this.artistes = res.map(oeuvre=> ({nom: oeuvre.auteur}))
            });
        }

    }
})


