from flask import*
app = Flask(__name__)

@app.route("/index")
def home():
     return render_template(logindex.html)

@app.route("/login")
def login():
      error = None;
      if request.method == "POST":
          if request.form["pass"]  !="AAA":
                error = "Invalid user"
           else:
               flash("Successfully logged in")
               return redirect(url_for("home"))
           return render_template("log.html", error = error)


app.run()