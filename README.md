# Soil Nutrient Analysis with Automated Recommendation System

## Overview

The Soil Nutrient Analysis with Automated Recommendation System is an IoT and Machine Learning based project designed to monitor soil health in real time and provide intelligent recommendations to farmers.

The system uses an ESP32 microcontroller connected to an NPK Soil Sensor to collect soil parameters such as Nitrogen (N), Phosphorus (P), Potassium (K), pH, temperature, moisture, and electrical conductivity (EC). The collected data is transmitted to a Flask-based web server where it is analyzed and displayed on a dashboard.

An XGBoost Machine Learning model is used to recommend suitable crops based on soil conditions. The system also provides fertilizer recommendations and supports weather-based rainfall analysis using the OpenWeatherMap API.

---

## Features

* Real-time soil nutrient monitoring using ESP32.
* NPK, pH, temperature, moisture, and EC measurement.
* Live web dashboard for sensor data visualization.
* Crop recommendation using XGBoost Machine Learning model.
* Fertilizer recommendation based on nutrient deficiencies.
* Weather API integration for rainfall analysis.
* Flask-based backend server.
* Responsive web interface for easy monitoring.

---

## System Architecture

NPK Sensor → ESP32 → Flask Server → Database/Memory → Web Dashboard → Crop & Fertilizer Recommendation

---

## Hardware Components

* ESP32 Development Board
* NPK Soil Sensor (RS485 Modbus)
* MAX485 TTL to RS485 Module
* Jumper Wires
* USB Cable
* Power Supply

---

## Software Technologies

* Python
* Flask
* HTML
* CSS
* JavaScript
* XGBoost
* NumPy
* OpenWeatherMap API
* Arduino IDE

---

Project_Folder/
│
├── app.py                      # Main Flask backend server
├── xgboost_soil_model.pkl      # Trained XGBoost crop recommendation model
├── label_encoder.pkl           # Converts model output into crop names
├── crop_ideal_values.json      # Ideal NPK values for fertilizer recommendation
│
└── templates/
    ├── index.html              # Main dashboard page
    ├── mode1.html              # Fertilizer recommendation page
    └── mode2.html              # Crop recommendation page
```

## Working Principle

1. The NPK sensor measures soil parameters.
2. ESP32 reads sensor values using Modbus RS485 communication.
3. Sensor data is converted into JSON format.
4. ESP32 sends data to the Flask server through Wi-Fi.
5. Flask stores the latest sensor data.
6. The dashboard fetches and displays real-time values.
7. The XGBoost model predicts the most suitable crop.
8. Fertilizer recommendations are generated based on nutrient deficiencies.
9. Weather API provides rainfall information for better recommendations.

---

## Machine Learning Model

Algorithm Used:

* XGBoost Classifier

Input Parameters:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH
* Rainfall

Output:

* Recommended Crop

---

## Applications

* Smart Agriculture
* Precision Farming
* Soil Health Monitoring
* Crop Recommendation Systems
* Fertilizer Optimization
* Agricultural Research

---

## Future Enhancements

* Cloud Database Integration
* Mobile Application
* Historical Data Analysis
* SMS Notifications
* AI-based Disease Detection
* Multi-Sensor Support

---

## Author

**Dewang Guruprasad Korgaonkar**

Bachelor of Engineering (Electronics & Telecommunication)

Finolex Academy of Management and Technology

GitHub: https://github.com/dewangkorgaonkar13-beep

---

## License

This project is developed for educational and research purposes.
