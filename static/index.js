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

const vueApp = new Vue({
    el: '#app',
    data: {
        message: `Hello Vue! Random Number: ${Math.random()}`,
        oeuvres: [
            {
                nom: 'test',
                auteur: 'Inconnu',
                dateCreation: '01/02/1322',
                type: 'Dessin',
                description: 'Courte description'
            },
            {
                nom: 'test2',
                auteur: 'No',
                dateCreation: '01/02/1322',
                type: 'Dessin',
                description: 'Courte description'
            }
        ]
    },
    delimiters: ['[[', ']]'],
    methods: {
    }
});