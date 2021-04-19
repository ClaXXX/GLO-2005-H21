async function connection(form) {
    return fetch(`/connection`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form)
    });
}

async function creer_compte(form) {
    return fetch('/creer_compte', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form)
    })
}

async function deconnection() {
    return fetch('/deconnection', { method: 'PUT' });
}

async function devenirArtiste(nom) {
    return fetch('/artiste/devenir', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({nom})
    })
}
async function fermerArtiste() {
    return fetch('/artiste/finir', {
        method: 'DELETE',
    })
}

async function fetch_oeuvre() {
    return fetch(`/oeuvre`, {
        method: 'GET'
    }).then(function (response) {
                return response.json()
            }).then(function(data){
                return data.oeuvre
            })
}
async function fetch_artiste() {
    return fetch(`/artiste`, {
        method: 'GET'
    }).then(function (response) {
                return response.json()
            }).then(function(data){
                return data.artiste
            })
}

async function rechercher(recherche, type) {
    return fetch(`/search/?type=${type}&recherche=${recherche}`, {
        method: 'GET'
    }).then(function (response) {
                return response.json()
            }).then(function(data){
                return data.oeuvre
            })
}

async function creer_oeuvre(form) {
    return fetch('/oeuvre/creer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form)
    })
}
async function supprimer_oeuvre(nom,auteur) {
    return fetch('/oeuvre/supprimer', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({nom,auteur},)
    })
}

// Commandes
async function fetch_commandes() {
    return fetch('/commande', { method: 'GET' })
        .then(res => res.json()).then(data => data.commandes);
}

async function fetch_commentaires(num) {
    return fetch(`/commande/${num}/commentaires`, { method: 'GET' })
        .then(res => res.json()).then(data => data.commentaires);
}

async function ajoute_commentaire(numero, texte) {
    return fetch(`/commande/${numero}/ajouteCommentaire`, {
        method: 'POST',
                headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({texte})
    });
}