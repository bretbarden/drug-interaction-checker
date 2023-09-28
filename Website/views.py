# Store standard roots in Wesbite (main directory)
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
import requests
from .models import  Query, User
from . import db

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    print ("Hi I am a route")
    query = None
    if request.method == "POST":
        medicationA = request.form.get("medicationA").strip() if request.form.get("medicationA") else None
        medicationB = request.form.get("medicationB").strip() if request.form.get("medicationB") else None

        print(medicationA, medicationB, "I WORK YAY")

        # responseA = requests.get( f"https://api.fda.gov/drug/label.json/?api_key=1tBoJ0npQzVMLDVsMWgzHVqySLpyrzSyfGk8EhsO&search=openfda.generic_name:{medicationA}").json()["results"][0]["drug_interactions"][0]



        responseB = requests.get(f"https://api.fda.gov/drug/label.json/?api_key=1tBoJ0npQzVMLDVsMWgzHVqySLpyrzSyfGk8EhsO&search=openfda.generic_name:{medicationB}").json()["results"][0]["drug_interactions"][0]


        try:

            responseA = requests.get(f"https://api.fda.gov/drug/label.json/?api_key=1tBoJ0npQzVMLDVsMWgzHVqySLpyrzSyfGk8EhsO&search=openfda.generic_name:{medicationA}").json()
              
            
            if responseA["results"][0]["drug_interactions"][0]:
                interactionA = responseA["results"][0]["drug_interactions"][0]

            
            elif responseA["results"][0]["warnings"][0]:
                interactionA = ["results"][0]["warnings"][0]

            else:
                interactionA = "Drug found in FDA records, but FDA query found no intearctions or warnings"

            print(interactionA)


        except:
            
            return {"error" : "Drug not found in FDA records; Please check to make sure you're using the generic name and try again"}

                    

        responseB = requests.get(f"https://api.fda.gov/drug/label.json/?api_key=1tBoJ0npQzVMLDVsMWgzHVqySLpyrzSyfGk8EhsO&search=openfda.generic_name:{medicationB}").json()
            


        query = Query(medicationA=medicationA, medicationB=medicationB, interactionA=interactionA, interactionB= responseB, user_id=current_user.id)
        db.session.add(query)
        db.session.commit()
        # print(query.interactionB)
        # return query.interactionB

        # return f"{responseA} + 'FIILLER FILLER FILLER' {responseB}"


    return render_template("home.html", user=current_user, query=query)





@views.route("/queries", methods=["GET", "POST"])
@login_required
def checkqueries():
    if request == "GET":
        users = User.query.all()
        return jsonify([{"id": u.id, "username": u.username} for u in users])
    return render_template("queries.html", user=current_user )

    









