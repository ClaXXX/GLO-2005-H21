Vue.component('oeuvre', {
  props: ['nom', 'auteur', 'dateCreation', 'type', 'description'],
  template: '  ' +
      '<div class="card col-3 m-3">' +
      '    <img class="card-img-top" src="/static/assets/logo.svg" alt="Card image cap">' +
      '    <div class="card-body">' +
      '      <h5 class="card-title">{{nom}} -- {{auteur}}</h5>' +
      '      <p class="card-text">{{type}}</p>' +
      '      <p class="card-text">{{description}}</p>' +
      '      <p class="card-text"><small class="text-muted">{{dateCreation}}</small></p>' +
      '    </div>' +
      '  </div>'
})
Vue.component('artiste', {
    props: ['nom', 'courriel'],
    template: '  ' +
        '<div class="card col-3 m-3">' +
        '    <img class="card-img-top" src="/static/assets/logo.svg" alt="Card image cap">' +
        '    <div class="card-body">' +
        '      <h5 class="card-title">{{nom}} </h5>' +
        '      <p class="card-text"><small class="text-muted">{{courriel}}</small></p>' +
        '    </div>' +
        '  </div>'
})
Vue.component('recherche',{
    props: ['recherche', 'type_recherche'],
})

async function fetch_oeuvre() {
    return fetch(`/oeuvre`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    }).then(function (response) {
                return response.json()
            }).then(function(data){
                return data.oeuvre
            })
}
async function fetch_artiste() {
    return fetch(`/artiste`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    }).then(function (response) {
                return response.json()
            }).then(function(data){
                return data.artiste
            })
}

async function rechercher(recherche, type) {
    return fetch(`/search/?type=${type}&recherche=${recherche}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    }).then(function (response) {
                return response.json()
            }).then(function(data){
                return data.oeuvre
            })
}


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
        onSearch: async function(event){
            event.preventDefault();
            await rechercher(this.recherche,this.type_recherche).then(res=>console.log(res));
        }

    }
})


