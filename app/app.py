from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    response = jsonify({
        "message": "DevSecOps test application is running",
        "status": "healthy"
    })

    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'self'"

    return response


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
