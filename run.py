from app import create_app

app = create_app()

if __name__ == '__main__':
    print("App is running fine")
    app.run(debug=True)