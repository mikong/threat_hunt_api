from flask import Flask, render_template
import connexion

app = connexion.App(__name__, specification_dir="openapi/")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
