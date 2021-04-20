async function handleResponse(response) {
    contenu = await response.json();
    if (!response.ok) {
        throw Error(contenu.message);
    }
    return contenu;
}


async function connection(form) {
    return fetch(`/connection`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form)
    }).then(handleResponse);
}

async function creer_compte(form) {
    return fetch('/creer_compte', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form)
    }).then(handleResponse)
}

async function deconnection() {
    return fetch('/deconnection', { method: 'PUT' }).then(handleResponse);
}

async function devenirArtiste(nom) {
    return fetch('/artiste/devenir', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({nom})
    }).then(handleResponse)
}
async function fermerArtiste() {
    return fetch('/artiste/finir', {
        method: 'DELETE',
    }).then(handleResponse)
}

async function fetch_oeuvre() {
    return fetch(`/oeuvre`, {
        method: 'GET'
    }).then(handleResponse)
        .then(function(data){
                return data.oeuvre
            })
}
async function fetch_artiste() {
    return fetch(`/artiste`, {
        method: 'GET'
    }).then(handleResponse)
        .then(function(data){
                return data.artiste
            })
}

async function rechercher(recherche, type) {
    return fetch(`/search/?type=${type}&recherche=${recherche}`, {
        method: 'GET'
    }).then(handleResponse)
        .then(function(data){
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
    }).then(handleResponse)
}
async function supprimer_oeuvre(nom,auteur) {
    return fetch('/oeuvre/supprimer', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({nom,auteur},)
    }).then(handleResponse)
}

// Commandes
async function fetch_commandes() {
    return fetch('/commande', { method: 'GET' })
        .then(handleResponse).then(data => data.commandes);
}

async function reserver(form) {
    return fetch('/commande/reserver', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form)
    }).then(handleResponse).then(data => data.commande);
}

async function creer(form) {
    return fetch('/commande/creer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form)
    }).then(handleResponse).then(data => data.commande);
}

async function fetch_artiste_commandes() {
    return fetch('/commande/artiste', { method: 'GET' })
        .then(handleResponse).then(data => data.commandes);
}

async function fetch_commentaires(num) {
    return fetch(`/commande/${num}/commentaires`, { method: 'GET' })
        .then(handleResponse).then(data => data.commentaires);
}

async function ajoute_commentaire(numero, texte) {
    return fetch(`/commande/${numero}/ajouteCommentaire`, {
        method: 'POST',
                headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({texte})
    }).then(handleResponse);
}