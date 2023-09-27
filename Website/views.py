# Store standard roots in Wesbite (main directory)
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
import requests
from .models import  Query
from . import db

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    print ("Hi I am a route")
    if request.method == "POST":
        medicationA = request.form.get("medicationA").strip() if request.form.get("medicationA") else None
        medicationB = request.form.get("medicationB").strip() if request.form.get("medicationB") else None

        print(medicationA, medicationB, "I WORK YAY")

        responseA = requests.get( f"https://api.fda.gov/drug/label.json/?api_key=1tBoJ0npQzVMLDVsMWgzHVqySLpyrzSyfGk8EhsO&search=openfda.generic_name:{medicationA}").json()["results"][0]["drug_interactions"][0]



        responseB = requests.get(f"https://api.fda.gov/drug/label.json/?api_key=1tBoJ0npQzVMLDVsMWgzHVqySLpyrzSyfGk8EhsO&search=openfda.generic_name:{medicationB}").json()["results"][0]["drug_interactions"][0]

        query = Query(medicationA=medicationA, medicationB=medicationB, user_id=current_user.id)
        db.session.add(query)
        db.session.commit()
        print(query)

        return f"{responseA} + 'FIILLER FILLER FILLER' {responseB}"


      


    return render_template("home.html", user=current_user)






