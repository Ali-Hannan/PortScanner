from flask import Flask, request, jsonify
from main import portScan  # import portScan function from main.py
from flask_cors import CORS  

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow CORS from all origins

# Test route to verify server is up
@app.route('/')
def home():
    return "Port Scanner API is running."

# /scan POST endpoint
@app.route('/scan', methods=['POST'])
def scan_ports():
    data = request.get_json()

    tgtHost = data.get("host")
    tgtPorts = data.get("ports")

    if not tgtHost or not tgtPorts:
        return jsonify({"error": "Missing host or ports"}), 400

    try:
        results = portScan(tgtHost, tgtPorts)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
