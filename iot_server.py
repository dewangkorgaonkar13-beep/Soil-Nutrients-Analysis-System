from flask import Flask, request, jsonify

app = Flask(__name__)

latest_data = {}

@app.route("/esp32-data", methods=["POST"])
def receive_data():
    global latest_data
    data = request.json
    latest_data = data
    print("Received from ESP32:", data)
    return jsonify({"status": "success", "stored": True})

@app.route("/get-latest", methods=["GET"])
def get_latest():
    return jsonify({"sensor_data": latest_data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)
