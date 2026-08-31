from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "DevSecOps pipeline demonstration is running."

@app.get("/health")
def health():
    return {"status": "healthy"}, 200
