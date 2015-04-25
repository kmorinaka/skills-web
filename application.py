from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    
    return "<html><body>This is the homepage.</body></html>"

    # # Alternately, we could make this a Jinja template in `templates/`
    # # and return that result of rendering this, like:
    # #
@app.route("/index")
def home_page():
    return render_template("index.html")

@app.route("/application-form")
def app_form():
    return render_template("application-form.html")

@app.route("/application", methods=["POST", "GET"])
def application():
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary_req = request.form.get("salaryreq")
    job_title = request.form.get("jobtitle")


    return render_template("application.html", firstname = first_name, 
        lastname = last_name, salaryreq = salary_req, jobtitle = job_title)


if __name__ == "__main__":
    app.run(debug=True)