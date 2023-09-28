# run this file to run webserver from wesbite by impotying create app module
from Website import create_app

app = create_app()
print("weep woop")

if __name__ == "__main__":
    print("beep boop")
    app.run(debug=True)