'''def login(client, username, password):
    return client.post('/login', data=dict(
        courriel=username,
        motpasse=password
    ), follow_redirects=True)

def test_login_logout(client):
    rv = login(client, flaskr.app.config['USERNAME'], flaskr.app.config['PASSWORD'])
    assert b'You were logged in' in rv.data
'''