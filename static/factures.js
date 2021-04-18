const facturesApp = new Vue({
    el: '#factures',
    delimiters: ['[[', ']]'],
    data: {
        factures: {
            numF: '',
            numC:'',
            adresse: '',
            total: '',
        }
    },
});