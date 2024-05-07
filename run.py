from app import create_app

app = create_app()

if __name__ == '__main__':
    # Disable the automatic reloader
    app.run(debug=False, use_reloader=False)
