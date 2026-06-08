from flask import Flask, render_template, request, jsonify
import pickle
import json
import numpy as np
import requests

app = Flask(__name__)

# =========================================================
# CONFIGURATION
# =========================================================
WEATHER_API_KEY = "e838543e6d7fd676ba6b0640768f97a2"

# =========================================================
# GLOBAL SENSOR DATA
# =========================================================
latest_sensor_data = {
    "N": 0,
    "P": 0,
    "K": 0,
    "ph": 7.0,
    "temperature": 25.0,
    "humidity": 50.0,
    "moisture": 50.0,
    "ec": 0,
    "rainfall": 0.0,
    "lat": 0.0,
    "lon": 0.0
}

# =========================================================
# LOAD ML MODEL
# =========================================================
model = None
label_encoder = None
crop_ideal = {}

try:
    with open("xgboost_soil_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)

    print("✅ XGBoost Model Loaded")

except Exception as e:
    print("⚠️ Model Load Error:", e)

# =========================================================
# LOAD FERTILIZER DATABASE
# =========================================================
try:
    with open("crop_ideal_values.json", "r") as f:
        crop_ideal = json.load(f)

    print("✅ Fertilizer Database Loaded")

except Exception as e:
    print("⚠️ JSON Load Error:", e)

# =========================================================
# WEB ROUTES
# =========================================================
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/mode1")
def mode1_page():
    crops = sorted(crop_ideal.keys()) if crop_ideal else []
    return render_template("mode1.html", crops=crops)

@app.route("/mode2")
def mode2_page():
    return render_template("mode2.html")

# =========================================================
# ESP32 DATA ROUTE
# =========================================================
@app.route("/esp32-data", methods=["POST"])
def receive_data():
    global latest_sensor_data

    try:
        # safer JSON parsing
        data = request.get_json(force=True)

        print("📡 Data received from ESP32:", data)

        latest_sensor_data["N"] = float(data.get("N", 0))
        latest_sensor_data["P"] = float(data.get("P", 0))
        latest_sensor_data["K"] = float(data.get("K", 0))
        latest_sensor_data["ph"] = float(data.get("ph", 7))
        latest_sensor_data["temperature"] = float(data.get("temperature", 25))
        latest_sensor_data["moisture"] = float(data.get("moisture", 50))
        latest_sensor_data["ec"] = float(data.get("ec", 0))
        latest_sensor_data["rainfall"] = float(data.get("rainfall", 0))

        return jsonify({
            "status": "success"
        }), 200

    except Exception as e:
        print("❌ ESP32 Error:", e)
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

# =========================================================
# WEBSITE LIVE DATA
# =========================================================
@app.route("/latest-data")
def get_latest():
    return jsonify({
        "sensor_data": latest_sensor_data
    })

# =========================================================
# WEATHER API
# =========================================================
@app.route("/update-location", methods=["POST"])
def update_location():
    global latest_sensor_data

    try:
        coords = request.get_json()

        lat = coords.get("latitude")
        lon = coords.get("longitude")

        latest_sensor_data["lat"] = lat
        latest_sensor_data["lon"] = lon

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"

        response = requests.get(url).json()

        rain_val = response.get("rain", {}).get("1h", 0)

        latest_sensor_data["rainfall"] = float(rain_val)

        print(f"🌧 Rain updated: {rain_val}")

        return jsonify({
            "status": "success",
            "rainfall": rain_val
        })

    except Exception as e:
        print("❌ Weather API Error:", e)

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# =========================================================
# MODE 1 → FERTILIZER
# =========================================================
@app.route("/api/mode1", methods=["POST"])
def fertilizer_logic():
    try:
        data = request.get_json()
        crop = data.get("crop", "").lower()

        ideal = crop_ideal.get(crop)

        if not ideal:
            return jsonify({
                "error": "Crop not found"
            }), 404

        result = {
            "Urea_needed": round(max(0, ideal["N"] - latest_sensor_data["N"]) * 2.17, 2),
            "DAP_needed": round(max(0, ideal["P"] - latest_sensor_data["P"]) * 2.17, 2),
            "MOP_needed": round(max(0, ideal["K"] - latest_sensor_data["K"]) * 1.67, 2)
        }

        return jsonify({
            "fertilizer_plan": result
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

# =========================================================
# MODE 2 → CROP RECOMMENDATION
# =========================================================
@app.route("/api/mode2", methods=["POST"])
def crop_recommendation():
    try:
        features = np.array([[
            latest_sensor_data["N"],
            latest_sensor_data["P"],
            latest_sensor_data["K"],
            latest_sensor_data["temperature"],
            latest_sensor_data["humidity"],
            latest_sensor_data["ph"],
            latest_sensor_data["rainfall"]
        ]])

        prediction_id = model.predict(features)[0]

        crop_name = label_encoder.inverse_transform(
            [int(prediction_id)]
        )[0]

        return jsonify({
            "recommended_crop": crop_name,
            "status": "success"
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# =========================================================
# RUN APP
# =========================================================
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=7000,
        debug=True
    )