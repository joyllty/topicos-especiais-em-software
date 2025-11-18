from flask import Flask, render_template
from controller.personagem_controller import blueprint_personagem

app = Flask(__name__)
app.register_blueprint(blueprint_personagem)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
