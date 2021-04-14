

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
        }
    }
})