import pytest
from src.index import create_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    # db_fd, db_path = tempfile.mkstemp()
    # create the app with common test config
    app = create_app(__name__)
    app.config.update({"TESTING": True})

    yield app


'''
    # create the database and load test data
    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)
'''

# close and remove the temporary database
'''
    os.close(db_fd)
    os.unlink(db_path)'''


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()


def test_empty_db(app):
    """Start with a blank database."""
    rv = client.get('/')
    print(rv.data)
    assert b'Bonjour.' in rv.data
