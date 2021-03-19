import pytest
from .. import main

@pytest.fixture
def app():
    app = main.create_app()
    return app


def test_empty_db(app):
    """Start with a blank database."""
    rv = app.get('/')
    print(rv.data)
    assert b'Bonjour.' in rv.data
