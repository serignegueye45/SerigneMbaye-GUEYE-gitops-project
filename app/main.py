from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Prénom Nom - Projet GitOps", "status": "ok"}

@app.route("/api/whoami")
def whoami():
    return {"student": "prenom-nom"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
