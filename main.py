# run this file to run webserver from wesbite by impotying create app module
from Website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)