from src.index import create_app


flask_app = create_app(__name__)
if __name__ == "__main__":
    flask_app.run()
