from flask import Flask, render_template, request, redirect
import os
import csv

app = Flask(__name__)


# home page
@app.route("/")
@app.route("/index.html")
def home():
    return render_template("./index.html")


# all other
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_db(data):
    with open("database.txt", "a") as my_db:
        my_db.write(f"\n{str(data)}")


def write_to_csv(data):
    with open("db.csv", newline="", mode="a") as my_db2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            my_db2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("./thankyou.html")
        except:
            return "data was not saved to db"
    else:
        return "Error: something went wrong. try again"
