Vue.component('suppression',{
    props:['nom','auteur','currentuser'],
    methods:{
        supprimeOeuvre: function (event,auteur,nom) {
            event.preventDefault();
            supprimer_oeuvre(nom, auteur)
                .then(res => {
                    if (res.status === 200)
                        window.location.reload()
                })
        }
    },
    template: '  ' +
        '<button class="btn btn-primary float-right" v-on:click="supprimeOeuvre($event,auteur,nom)" style="margin-top: 20px" type="button"> Supprimer cette oeuvre </button>'
})
Vue.component('oeuvre', {
  props: ['nom', 'auteur', 'date', 'type', 'description', 'currentuser', 'expose'],
  methods: {
    command_text: function () {
        if (typeof this.expose != 'undefined' && this.currentuser === this.auteur)
            return '<div class="float-right"> ' + (this.expose === '1' ? 'exposée' : 'non exposée') + '</div>'
        return ''
    },
    emit_click: function () {
        this.$emit('click');
    }
  },
  template: '  ' +
      '<div class="card my-2 border-0">' +
      '  <div class="horizontal-card row">' +
      '    <img class="card-img col-3" src="/static/assets/logo.svg" alt="Card image cap">' +
      '    <div class="card-body col-9" style="padding-left: 10px">' +
      '      <div class="text-muted" v-html="command_text()"></div>' +
      '      <div class="card-title oeuvre-titre">{{nom}}</div>' +
      '      <div class="card-text">{{type}}</div>' +
      '      <p class="card-text">{{description}}</p>' +
      '    </div>' +
      '  </div>' +
      '<suppression :nom="nom" :auteur="auteur" v-if="currentuser===auteur">'+
      '</suppression>'+
      '<button v-if="currentuser !== undefined && currentuser!==auteur" class="btn btn-primary" type="button" data-toggle="modal" data-target="#reservation-oeuvre-modal" v-on:click="emit_click()" > Commander'+
      '</button>'+
      '  <div class="card-footer oeuvre-footer">' +
      '     <small class="text-muted">{{date}}</small> ' +
      '<a class="float-right" v-bind:href="\'/artiste/\' + this.auteur">{{auteur}}</a>' +
      '  </div> ' +
      '</div>'
})
Vue.component('artiste', {
    props: ['nom', 'courriel'],
    template: '  ' +
        '<a class="card m-2" style="float: left;" v-bind:href="\'/artiste/\' + this.nom">' +
        '    <img class="card-img-top" style="width: 256px" src="/static/assets/logo.svg" alt="Card image cap">' +
        '    <div class="card-body">' +
        '      <h5 class="card-title">{{nom}} </h5>' +
        '      <p class="card-text"><small class="text-muted">{{courriel}}</small></p>' +
        '    </div>' +
        '  </a>'
})
Vue.component('commande', {
    props: ['num', 'superviseur', 'statut', 'prix', 'type'],
    template: '' +
      '<div class="card my-2 border-0">' +
      '  <div class="horizontal-card row">' +
      '    <img class="card-img col-3" src="/static/assets/logo.svg" alt="Card image cap">' +
      '    <div class="card-body col-9" style="padding-left: 10px">' +
      '      <small class="float-right text-muted"> {{statut}}</small>' +
      '      <div class="card-title oeuvre-titre">{{superviseur}}</div>' +
      '      <small class="card-text float-right">{{num}}</small>' +
      '    </div>' +
      '  </div>' +
      '</div>'
});

Vue.component('recherche',{
    props: ['recherche', 'type_recherche'],
})