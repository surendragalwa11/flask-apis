from app import create_app

if __name__ == '__main__':
    app = create_app("app.config")
    app.run(debug=True)