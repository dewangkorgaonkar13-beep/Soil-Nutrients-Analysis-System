const express = require("express");
const axios = require("axios");
const path = require("path");

const app = express();

// ------------------ Middleware ------------------
app.use(express.json());

// Serve frontend files
app.use(express.static(path.join(__dirname, "public")));

// ------------------ API URLs ------------------
const ML_API = "http://127.0.0.1:5000/predict";        // ML Flask server
const IOT_GET = "http://127.0.0.1:7000/get-latest";

 // IoT Flask server (PC IP)

// ------------------ HOME ROUTE ------------------
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

// ------------------ LIVE IOT DATA ------------------
app.get("/api/live-iot", async (req, res) => {
  try {
    const response = await axios.get(IOT_GET);
    res.json(response.data);
  } catch (error) {
    console.error("IoT fetch error:", error.message);
    res.status(500).json({
      status: "error",
      message: "IoT server not reachable"
    });
  }
});

// ------------------ IOT → ML → WEBSITE ------------------
app.get("/api/iot-predict", async (req, res) => {
  try {
    // 1. Get latest ESP32 data
    const iotRes = await axios.get(IOT_GET);
    const sensor = iotRes.data.sensor_data;

    if (!sensor || !sensor.temp || !sensor.humidity) {
      return res.json({
        status: "waiting",
        message: "Waiting for ESP32 data"
      });
    }

    // 2. Add default values for missing ML features
    const mlInput = {
      n: 50,          // default nitrogen
      p: 40,          // default phosphorus
      k: 40,          // default potassium
      ph: 6.5,        // default pH
      moisture: 30,   // default moisture
      temp: sensor.temp,
      humidity: sensor.humidity,
      rainfall: 100   // default rainfall
    };

    // 3. Send to ML server
    const mlRes = await axios.post(ML_API, mlInput);

    // 4. Send to website
    res.json({
      status: "success",
      sensor_data: sensor,
      prediction: mlRes.data.prediction
    });

  } catch (error) {
    console.error("IoT→ML error:", error.message);
    res.status(500).json({
      status: "error",
      message: "IoT or ML server error"
    });
  }
});

// ------------------ MANUAL FORM → ML ------------------
app.post("/api/predict", async (req, res) => {
  try {
    console.log("Manual input from website:", req.body);

    const mlRes = await axios.post(ML_API, req.body);

    res.json({
      status: "success",
      prediction: mlRes.data.prediction,
      model: "XGBoost"
    });

  } catch (error) {
    console.error("Manual ML error:", error.message);
    res.status(500).json({
      status: "error",
      message: "ML server not responding"
    });
  }
});

// ------------------ SERVER START ------------------
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Website running at http://localhost:${PORT}`);
});
