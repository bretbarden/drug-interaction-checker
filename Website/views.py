# Store standard roots in Wesbite (main directory)
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
import requests
from .models import  Query, User, Note
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

        # Query the FDA databse for medication A by generic name, returning interactions if found, warnings if no interactions found, and an error message if nothing found
        try:

            responseA = requests.get(f"https://api.fda.gov/drug/label.json/?api_key=1tBoJ0npQzVMLDVsMWgzHVqySLpyrzSyfGk8EhsO&search=openfda.generic_name:{medicationA}").json()
            print(responseA)
            
            if "drug_interactions" in responseA["results"][0]:
                interactionA = responseA["results"][0]["drug_interactions"][0]
                print(responseA["results"][0]["drug_interactions"][0])
                print(f'**************************{interactionA} comes from "drug_interactions"**********************')

            elif "warnings" in responseA["results"][0]:
                interactionA = responseA["results"][0]["warnings"][0]
                print(f' ********************** {interactionA} comes from "warnings" ************************')

            else:
                interactionA = "Drug A found in FDA records, but FDA query found no intearctions or warnings"
                print(f'**************************{interactionA}**************************')

        except:
            
            return {"error" : "Drug A not found in FDA records; Please check to make sure you're using the generic name and try again"}
        


        # Query the FDA databse for medication B by generic name, returning interactions if found, warnings if no interactions found, and an error message if nothing found
        if medicationB is not None:
            try:

                responseB = requests.get(f"https://api.fda.gov/drug/label.json/?api_key=1tBoJ0npQzVMLDVsMWgzHVqySLpyrzSyfGk8EhsO&search=openfda.generic_name:{medicationB}").json()
                print(responseB)
                
                if "drug_interactions" in responseB["results"][0]:
                    interactionB = responseB["results"][0]["drug_interactions"][0]
                    print(responseB["results"][0]["drug_interactions"][0])
                    print(f'**************************{interactionB} comes from "drug_interactions"**********************')

                elif "warnings" in responseB["results"][0]:
                    interactionB = responseB["results"][0]["warnings"][0]
                    print(f' ********************** {interactionB} comes from "warnings" ************************')

                else:
                    interactionB = "Drug B found in FDA records, but FDA query found no intearctions or warnings"
                    print(f'**************************{interactionB}**************************')


            except:
                
                return {"error" : "Drug B not found in FDA records; Please check to make sure you're using the generic name and try again"}

                    

        ## TO DO ##

        ## BUILD OUT SEARCHES FOR BRAND NAMES ##



        # Replace with  interactionB = interactionB once all logic worked out and copied from A
        query = Query(medicationA=medicationA, medicationB=medicationB, interactionA=interactionA, interactionB= interactionB, user_id=current_user.id)

        db.session.add(query)
        db.session.commit()
        # print(query.interactionB)
        # return query.interactionB

        # return f"{responseA} + 'FIILLER FILLER FILLER' {responseB}"


    return render_template("home.html", user=current_user, query=query)





@views.route("/queries", methods=["GET", "POST"])
@login_required
def checkqueries():
    note = None
    query_id = None
    if request.method == "GET":
        queries = Query.query.filter_by(user_id=current_user.id).all()

    elif request.method == "POST":
        # query_id = request.form.get("data-query-id")
        user_id = current_user.id
        query_id = request.form.get("query_id") 
        print("this is the query id", query_id)
    

        # date = request.form.get("datesubmit")
        text = request.form.get("text")
        print(text)

        if text:
            note = Note(text=text, user_id=user_id, query_id=query_id)
            db.session.add(note)
            db.session.commit()
            print("I AM A NOTE", note.text)
        return redirect(url_for("views.showmyNotes"))
    return render_template("queries.html", user=current_user, user_id=current_user.id, note=note, queries=queries, query_id=query_id)





@views.route("/notes", methods=["GET"])
@login_required
def showmyNotes():
    notes = Note.query.all()
    print(notes)
    return render_template("notes.html", user=current_user, notes=notes)



# @views.route("/community-notes", methods=["GET", "POST"])
# @login_required
# def showallNotes():
        
#         notes = Note.query.all()
#         return render_template("notes.html", user=current_user, notes=notes)


    









