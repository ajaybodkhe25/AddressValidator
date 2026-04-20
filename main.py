from flask import Flask, request, jsonify
import address_validator

app = Flask(__name__)

@app.route("/")
def home():
    return "Address Validator Running 🚀"

@app.route("/validate", methods=["GET"])
def validate():
    address = request.args.get("address")

    if not address:
        return jsonify({"error": "No address provided"}), 400

    result = address_validator.validate(address)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
