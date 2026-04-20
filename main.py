from flask import Flask, request, jsonify
import address_validator  # or whatever the original file name is

app = Flask(__name__)

@app.route("/")
def home():
    return "Address Validator is running!"

@app.route("/validate", methods=["GET"])
def validate():
    address = request.args.get("address")
    if not address:
        return jsonify({"error": "No address provided"})
    
    result = address_validator.validate(address)  # adjust based on actual function
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
